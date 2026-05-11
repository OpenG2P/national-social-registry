from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from sqlalchemy import Date, String, select
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceHouseholdProgram
from .enums import PaymentChannelPreferenceEnum, PaymentVerificationStatusEnum


class G2PHouseholdProgram:

    program_name: Mapped[str] = mapped_column(String, nullable=True)
    program_mnemonic: Mapped[str] = mapped_column(String, nullable=True, index=True)
    program_start_date: Mapped[Date] = mapped_column(Date, nullable=True, index=True)
    program_exit_date: Mapped[Date] = mapped_column(Date, nullable=True)
    legacy_program_id: Mapped[str] = mapped_column(String, nullable=True, index=True)

    payment_channel_preference: Mapped[PaymentChannelPreferenceEnum] = mapped_column(
        String, nullable=True
    )
    payment_account_token: Mapped[str] = mapped_column(String, nullable=True, index=True)
    payment_verification_status: Mapped[PaymentVerificationStatusEnum] = mapped_column(
        String, nullable=True
    )


class G2PRegisterHouseholdProgram(G2PRegister, G2PHouseholdProgram):
    __tablename__ = "g2p_register_household_programs"

    def get_search_text_fields(self) -> str:
        """Return household program fields used to build search_text."""
        return G2PRegisterDomainServiceHouseholdProgram().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return household program record_name from domain service implementation."""
        return G2PRegisterDomainServiceHouseholdProgram().construct_record_name(self.to_dict())


class G2PRegisterHistoryHouseholdProgram(G2PRegisterHistory, G2PHouseholdProgram):
    __tablename__ = "g2p_register_history_household_programs"


class G2PIntakeFormHouseholdProgram(G2PIntakeForm, G2PRegister, G2PHouseholdProgram):
    __tablename__ = "g2p_intake_form_household_programs"

    async def get_link_internal_record_id(self, session):
        from .household import G2PIntakeFormHousehold

        result = await session.execute(
            select(G2PIntakeFormHousehold).where(
                G2PIntakeFormHousehold.submission_id == self.submission_id
            )
        )
        household = result.scalars().first()
        if household:
            self.link_internal_record_id = household.internal_record_id

    def get_search_text_fields(self) -> str:
        """Return household program fields used to build search_text."""
        return G2PRegisterDomainServiceHouseholdProgram().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return household program record_name from domain service implementation."""
        return G2PRegisterDomainServiceHouseholdProgram().construct_record_name(self.to_dict())
