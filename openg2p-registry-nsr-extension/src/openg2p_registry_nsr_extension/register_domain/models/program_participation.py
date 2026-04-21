from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceProgramParticipation
from .enums import (
    LinkedRegisterMnemonicEnum,
    PaymentChannelPreferenceEnum,
    PaymentVerificationStatusEnum,
)


class G2PRegisterProgramParticipation(G2PRegister):
    __tablename__ = "g2p_register_program_participations"

    # link_internal_record_id -> Individual OR Household.internal_record_id
    linked_register_mnemonic: Mapped[LinkedRegisterMnemonicEnum] = mapped_column(String, nullable=True)

    program_name: Mapped[str] = mapped_column(String, nullable=True)        # attribute lookup (PROGRAM_NAME)
    program_mnemonic: Mapped[str] = mapped_column(String, nullable=True)
    program_start_date: Mapped[Date] = mapped_column(Date, nullable=True)
    program_exit_date: Mapped[Date] = mapped_column(Date, nullable=True)
    legacy_program_id: Mapped[str] = mapped_column(String, nullable=True)

    payment_channel_preference: Mapped[PaymentChannelPreferenceEnum] = mapped_column(String, nullable=True)
    payment_account_token: Mapped[str] = mapped_column(String, nullable=True)  # tokenised reference only
    payment_verification_status: Mapped[PaymentVerificationStatusEnum] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceProgramParticipation().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceProgramParticipation().construct_record_name(self.to_dict())


class G2PRegisterHistoryProgramParticipation(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_program_participations"

    linked_register_mnemonic: Mapped[str] = mapped_column(String, nullable=True)
    program_name: Mapped[str] = mapped_column(String, nullable=True)
    program_mnemonic: Mapped[str] = mapped_column(String, nullable=True)
    program_start_date: Mapped[Date] = mapped_column(Date, nullable=True)
    program_exit_date: Mapped[Date] = mapped_column(Date, nullable=True)
    legacy_program_id: Mapped[str] = mapped_column(String, nullable=True)
    payment_channel_preference: Mapped[str] = mapped_column(String, nullable=True)
    payment_account_token: Mapped[str] = mapped_column(String, nullable=True)
    payment_verification_status: Mapped[str] = mapped_column(String, nullable=True)
