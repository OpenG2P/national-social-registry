import logging
from datetime import date

from openg2p_registry_core.models import G2PRegisterChangeRequest
from openg2p_registry_core.services import G2PRegisterDomainService
from sqlalchemy.ext.asyncio import AsyncSession

from .domain_validation_utils import as_int, is_blank, parse_date, validation_error

_logger = logging.getLogger("g2p-register-domain-service")


class G2PRegisterDomainServiceIndividual(G2PRegisterDomainService):
    async def validate_domain_attributes(self, records: list[dict]):
        for record in records:
            self._validate_middle_name(record)
            self._validate_birth_date(record)
            self._validate_estimated_age(record)

    def _validate_middle_name(self, record: dict) -> None:
        if is_blank(record.get("middle_name")):
            validation_error("middle_name is required")

    def _validate_birth_date(self, record: dict) -> None:
        birth_date = parse_date(record.get("birth_date"))
        if birth_date is not None and birth_date > date.today():
            validation_error("birth_date must not be in the future")

    def _validate_estimated_age(self, record: dict) -> None:
        birth_date = parse_date(record.get("birth_date"))
        estimated_age = as_int(record.get("estimated_age"))
        if birth_date is None or estimated_age is None:
            return
        computed_age = self._calculate_age(birth_date)
        if computed_age is not None and abs(estimated_age - computed_age) > 1:
            validation_error(
                "estimated_age must be consistent with birth_date within one year"
            )

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for individual")

        keys = [
            "functional_record_id",
            "first_name",
            "last_name",
            "middle_name",
            "given_name",
            "full_name",
            "alias_names",
            "foundational_id",
            "foundational_id_masked",
            "gender",
            "birth_date",
            "estimated_age",
            "marital_status",
            "citizenship_category",
            "relationship_to_head",
            "primary_livelihood",
            "secondary_livelihood",
            "employment_status",
            "disability_status",
            "displacement_status",
            "pastoralist_classification",
            "latitude",
            "longitude",
            "altitude",
            "plus_code",
            "address_line_1",
            "address_line_2",
            "postal_code",
            "country_code",
        ]
        search_text = []
        if extra:
            search_text.extend(
                str(value).strip() for value in extra if str(value).strip()
            )
        search_text.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(search_text).strip()

    def construct_record_name(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing record name for individual")

        keys = ["first_name", "last_name"]
        record_name = []
        if extra:
            record_name.extend(str(item).strip() for item in extra if str(item).strip())
        record_name.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(record_name).strip()

    async def post_ingest(self, register_id: str, register_row, session: AsyncSession):
        from ..models.household import G2PRegisterHousehold

        link_internal_record_id = getattr(register_row, "link_internal_record_id", None)
        if not link_internal_record_id:
            return

        household = await session.get(G2PRegisterHousehold, link_internal_record_id)
        if not household:
            return

        birth_date = getattr(register_row, "birth_date", None)
        if birth_date:
            age = self._calculate_age(birth_date)
            if age is not None and age < 5:
                household.size_children_u5 = (household.size_children_u5 or 0) + 1

    async def post_approve(self, change_request: G2PRegisterChangeRequest, session: AsyncSession):
        from openg2p_registry_core.models import G2PRegisterChangeRequestPayload
        from ..models.household import G2PRegisterHousehold
        from ..models.individual import G2PRegisterIndividual

        payload_obj = await session.get(G2PRegisterChangeRequestPayload, change_request.change_request_id)
        if not payload_obj or not payload_obj.change_payload:
            return

        for record in payload_obj.change_payload:
            record_status = record.get("record_status")
            record_status_reason = record.get("record_status_reason")

            if record_status == "INACTIVE" and record_status_reason == "Death":

                individual = await session.get(G2PRegisterIndividual, change_request.internal_record_id)
                if not individual or not individual.link_internal_record_id:
                    continue

                household = await session.get(G2PRegisterHousehold, individual.link_internal_record_id)
                if not household:
                    continue

                household.husband_dead = True
                household.husband_dead_date = change_request.approved_at.date()

    @staticmethod
    def _calculate_age(birth_date):
        if not birth_date:
            return None
        today = date.today()
        return (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
