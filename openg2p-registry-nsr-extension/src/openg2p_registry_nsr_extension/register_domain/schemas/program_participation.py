from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import (
    LinkedRegisterMnemonicEnum,
    PaymentChannelPreferenceEnum,
    PaymentVerificationStatusEnum,
)


class G2PRegisterSchemaProgramParticipation(G2PRegisterBaseSchema):
    """
    Schema for ProgramParticipation.
    link_internal_record_id -> Individual OR Household.internal_record_id
    """
    linked_register_mnemonic: Optional[LinkedRegisterMnemonicEnum] = None
    program_name: Optional[str] = None
    program_mnemonic: Optional[str] = None
    program_start_date: Optional[date] = None
    program_exit_date: Optional[date] = None
    legacy_program_id: Optional[str] = None
    payment_channel_preference: Optional[PaymentChannelPreferenceEnum] = None
    payment_account_token: Optional[str] = None
    payment_verification_status: Optional[PaymentVerificationStatusEnum] = None


class G2PRegisterHistorySchemaProgramParticipation(G2PRegisterHistorySchema):
    linked_register_mnemonic: Optional[LinkedRegisterMnemonicEnum] = None
    program_name: Optional[str] = None
    program_mnemonic: Optional[str] = None
    program_start_date: Optional[date] = None
    program_exit_date: Optional[date] = None
    legacy_program_id: Optional[str] = None
    payment_channel_preference: Optional[PaymentChannelPreferenceEnum] = None
    payment_account_token: Optional[str] = None
    payment_verification_status: Optional[PaymentVerificationStatusEnum] = None
