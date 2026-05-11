from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PRegisterHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import PaymentChannelPreferenceEnum, PaymentVerificationStatusEnum


class G2PSchemaHouseholdProgram:

    program_name: Optional[str] = None
    program_mnemonic: Optional[str] = None
    program_start_date: Optional[date] = None
    program_exit_date: Optional[date] = None
    legacy_program_id: Optional[str] = None

    payment_channel_preference: Optional[PaymentChannelPreferenceEnum] = None
    payment_account_token: Optional[str] = None
    payment_verification_status: Optional[PaymentVerificationStatusEnum] = None


class G2PRegisterSchemaHouseholdProgram(G2PRegisterBaseSchema, G2PSchemaHouseholdProgram):
    """
    Schema for HouseholdProgram register.
    link_internal_record_id -> Household.internal_record_id
    """


class G2PRegisterHistorySchemaHouseholdProgram(G2PRegisterHistorySchema):
    """
    Schema for HouseholdProgram history.
    """


class G2PIntakeFormSchemaHouseholdProgram(
    G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PSchemaHouseholdProgram
):
    """
    Schema for HouseholdProgram intake form.
    """
