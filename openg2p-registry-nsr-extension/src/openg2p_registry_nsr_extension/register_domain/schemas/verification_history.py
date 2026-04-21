from datetime import datetime
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import (
    LinkedRegisterMnemonicEnum,
    RecordVerificationStatusEnum,
    UpdateTriggerEnum,
    VerificationMethodEnum,
)


class G2PRegisterSchemaVerificationHistory(G2PRegisterBaseSchema):
    """
    Schema for VerificationHistory.
    link_internal_record_id -> Individual OR Household.internal_record_id
    """
    linked_register_mnemonic: Optional[LinkedRegisterMnemonicEnum] = None
    update_trigger: Optional[UpdateTriggerEnum] = None
    data_source: Optional[str] = None
    enumerator_id: Optional[str] = None
    office_location_code: Optional[str] = None
    verification_status: Optional[RecordVerificationStatusEnum] = None
    verification_method: Optional[VerificationMethodEnum] = None
    verified_at: Optional[datetime] = None
    data_quality_flags: Optional[dict] = None


class G2PRegisterHistorySchemaVerificationHistory(G2PRegisterHistorySchema):
    linked_register_mnemonic: Optional[LinkedRegisterMnemonicEnum] = None
    update_trigger: Optional[UpdateTriggerEnum] = None
    data_source: Optional[str] = None
    enumerator_id: Optional[str] = None
    office_location_code: Optional[str] = None
    verification_status: Optional[RecordVerificationStatusEnum] = None
    verification_method: Optional[VerificationMethodEnum] = None
    verified_at: Optional[datetime] = None
    data_quality_flags: Optional[dict] = None
