from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import ConsentMethodEnum


class G2PRegisterSchemaConsent(G2PRegisterBaseSchema):
    """
    Schema for Consent.
    link_internal_record_id -> Individual.internal_record_id
    """
    consent_captured: Optional[bool] = None
    consent_date: Optional[date] = None
    consent_scope: Optional[dict] = None
    consent_method: Optional[ConsentMethodEnum] = None
    consent_evidence_ref: Optional[str] = None
    data_sharing_restrictions: Optional[dict] = None


class G2PRegisterHistorySchemaConsent(G2PRegisterHistorySchema):
    consent_captured: Optional[bool] = None
    consent_date: Optional[date] = None
    consent_scope: Optional[dict] = None
    consent_method: Optional[ConsentMethodEnum] = None
    consent_evidence_ref: Optional[str] = None
    data_sharing_restrictions: Optional[dict] = None
