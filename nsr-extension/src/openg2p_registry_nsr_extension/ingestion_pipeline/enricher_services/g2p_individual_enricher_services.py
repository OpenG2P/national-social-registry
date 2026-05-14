import logging
from typing import Any, Dict

from openg2p_registry_core.interfaces import G2PPayloadEnricherInterface
from sqlalchemy.orm import Session

_logger = logging.getLogger('g2p-payload-enricher-service')


def _merge_additional_attributes(raw: Any) -> Dict[str, Any]:
    """DO.SR.02 allows additional_attributes as 0…1 object or, in practice, a list of objects; merge into one dict (later keys win)."""
    merged: Dict[str, Any] = {}
    if isinstance(raw, dict):
        merged.update(raw)
    elif isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                merged.update(item)
    return merged


# DCI Payload Enrichers
class G2PDciIndividualCreateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PDciIndividualCreateEnricherService")
        if isinstance(data, dict):
            data["additional_attributes"] = _merge_additional_attributes(
                data.get("additional_attributes")
            )
        return data


class G2PDciIndividualUpdateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PDciIndividualUpdateEnricherService")
        return data


class G2PDciIndividualDeleteEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PDciIndividualDeleteEnricherService")
        return data


# SPDCI Payload Enrichers
class G2PSpdciIndividualCreateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PSpdciIndividualCreateEnricherService")
        return data


class G2PSpdciIndividualUpdateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PSpdciIndividualUpdateEnricherService")
        return data


class G2PSpdciIndividualDeleteEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PSpdciIndividualDeleteEnricherService")
        return data


# UNDP Payload Enrichers
class G2PUndpIndividualCreateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PUndpIndividualCreateEnricherService")
        return data


class G2PUndpIndividualUpdateEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PUndpIndividualUpdateEnricherService")
        return data


class G2PUndpIndividualDeleteEnricherService(G2PPayloadEnricherInterface):
    def enrich(self, data: Dict, session: Session) -> Dict:
        _logger.info("Processing G2PUndpIndividualDeleteEnricherService")
        return data
