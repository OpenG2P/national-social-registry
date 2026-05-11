from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from sqlalchemy import Date, String, select
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceIndividualProgram
from .enums import PaymentChannelPreferenceEnum, PaymentVerificationStatusEnum


class G2PIndividualProgram:

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


class G2PRegisterIndividualProgram(G2PRegister, G2PIndividualProgram):
    __tablename__ = "g2p_register_individual_programs"

    def get_search_text_fields(self) -> str:
        """Return individual program fields used to build search_text."""
        return G2PRegisterDomainServiceIndividualProgram().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return individual program record_name from domain service implementation."""
        return G2PRegisterDomainServiceIndividualProgram().construct_record_name(self.to_dict())


class G2PRegisterHistoryIndividualProgram(G2PRegisterHistory, G2PIndividualProgram):
    __tablename__ = "g2p_register_history_individual_programs"


class G2PIntakeFormIndividualProgram(G2PIntakeForm, G2PRegister, G2PIndividualProgram):
    __tablename__ = "g2p_intake_form_individual_programs"

    async def get_link_internal_record_id(self, session):
        from .individual import G2PIntakeFormIndividual

        result = await session.execute(
            select(G2PIntakeFormIndividual).where(
                G2PIntakeFormIndividual.submission_id == self.submission_id
            )
        )
        individual = result.scalars().first()
        if individual:
            self.link_internal_record_id = individual.internal_record_id

    def get_search_text_fields(self) -> str:
        """Return individual program fields used to build search_text."""
        return G2PRegisterDomainServiceIndividualProgram().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return individual program record_name from domain service implementation."""
        return G2PRegisterDomainServiceIndividualProgram().construct_record_name(self.to_dict())
