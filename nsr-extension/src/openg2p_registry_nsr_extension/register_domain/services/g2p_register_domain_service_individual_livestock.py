import logging

from openg2p_registry_core.services import G2PRegisterDomainService

from .domain_validation_utils import validation_error

_logger = logging.getLogger("g2p-register-individual-livestock-service")


class G2PRegisterDomainServiceIndividualLivestock(G2PRegisterDomainService):
    async def validate_domain_attributes(self, records: list[dict]):
        self._validate_no_duplicate_livestock_species(records)

    def _validate_no_duplicate_livestock_species(self, records: list[dict]) -> None:
        seen: set[str] = set()
        for record in records:
            value = record.get("livestock_species")
            if value is None or str(value).strip() == "":
                continue
            normalized = str(value).strip()
            if normalized in seen:
                validation_error("Duplicate livestock_species entries are not allowed")
            seen.add(normalized)

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for individual livestock")

        keys = ["functional_record_id", "livestock_species", "livestock_counts"]
        search_text = []
        if extra:
            search_text.extend(str(v).strip() for v in extra if str(v).strip())
        search_text.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )
        return " ".join(search_text).strip()

    def construct_record_name(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing record name for individual livestock")

        keys = ["functional_record_id"]
        record_name = []
        if extra:
            record_name.extend(str(v).strip() for v in extra if str(v).strip())
        record_name.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )
        return " ".join(record_name).strip()
