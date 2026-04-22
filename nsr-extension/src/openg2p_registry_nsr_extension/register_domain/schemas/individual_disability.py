from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import DisabilityDomainEnum, DisabilitySeverityEnum


class G2PRegisterSchemaIndividualDisability(G2PRegisterBaseSchema):
    """
    Schema for IndividualDisability.
    link_internal_record_id -> Individual.internal_record_id
    """
    disability_domain: Optional[DisabilityDomainEnum] = None
    disability_severity: Optional[DisabilitySeverityEnum] = None


class G2PRegisterHistorySchemaIndividualDisability(G2PRegisterHistorySchema):
    disability_domain: Optional[DisabilityDomainEnum] = None
    disability_severity: Optional[DisabilitySeverityEnum] = None
