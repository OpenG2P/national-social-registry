import logging

from openg2p_registry_core.services import G2PRegisterDomainService

from .domain_validation_utils import as_bool, as_float, is_blank, validation_error

_logger = logging.getLogger("g2p-register-individual-land-service")


class G2PRegisterDomainServiceIndividualLand(G2PRegisterDomainService):
    async def validate_domain_attributes(self, records: list[dict]):
        for record in records:
            self._validate_land_access(record)

    def _validate_land_access(self, record: dict) -> None:
        land_access = as_bool(record.get("land_access"))
        land_size = as_float(record.get("land_size"))
        productive_assets = record.get("productive_assets")

        if land_access is False:
            if land_size is not None and land_size > 0:
                validation_error("land_size must be empty when land_access is false")
            if not is_blank(productive_assets):
                validation_error("productive_assets must be empty when land_access is false")

        if land_access is True and (land_size is None or land_size <= 0):
            validation_error("land_size must be greater than zero when land_access is true")

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for individual land")

        keys = ["functional_record_id", "land_access", "land_size", "productive_assets"]
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
        _logger.info("Constructing record name for individual land")

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
