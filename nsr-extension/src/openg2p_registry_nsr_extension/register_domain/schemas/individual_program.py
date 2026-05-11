from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PRegisterHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import PaymentChannelPreferenceEnum, PaymentVerificationStatusEnum


class G2PSchemaIndividualProgram:

    program_name: Optional[str] = None
    program_mnemonic: Optional[str] = None
    program_start_date: Optional[date] = None
    program_exit_date: Optional[date] = None
    legacy_program_id: Optional[str] = None

    payment_channel_preference: Optional[PaymentChannelPreferenceEnum] = None
    payment_account_token: Optional[str] = None
    payment_verification_status: Optional[PaymentVerificationStatusEnum] = None


class G2PRegisterSchemaIndividualProgram(G2PRegisterBaseSchema, G2PSchemaIndividualProgram):
    """
    Schema for IndividualProgram register.
    link_internal_record_id -> Individual.internal_record_id
    """


class G2PRegisterHistorySchemaIndividualProgram(G2PRegisterHistorySchema):
    """
    Schema for IndividualProgram history.
    """


class G2PIntakeFormSchemaIndividualProgram(
    G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PSchemaIndividualProgram
):
    """
    Schema for IndividualProgram intake form.
    """
