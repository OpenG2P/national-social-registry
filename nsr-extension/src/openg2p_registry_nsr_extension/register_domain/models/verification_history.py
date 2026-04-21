from sqlalchemy import JSON, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceVerificationHistory
from .enums import (
    LinkedRegisterMnemonicEnum,
    RecordVerificationStatusEnum,
    UpdateTriggerEnum,
    VerificationMethodEnum,
)


class G2PRegisterVerificationHistory(G2PRegister):
    __tablename__ = "g2p_register_verification_history"

    # link_internal_record_id -> Individual OR Household.internal_record_id
    linked_register_mnemonic: Mapped[LinkedRegisterMnemonicEnum] = mapped_column(String, nullable=True)
    update_trigger: Mapped[UpdateTriggerEnum] = mapped_column(String, nullable=True)
    data_source: Mapped[str] = mapped_column(String, nullable=True)   # attribute lookup
    enumerator_id: Mapped[str] = mapped_column(String, nullable=True)
    office_location_code: Mapped[str] = mapped_column(String, nullable=True)
    verification_status: Mapped[RecordVerificationStatusEnum] = mapped_column(String, nullable=True)
    verification_method: Mapped[VerificationMethodEnum] = mapped_column(String, nullable=True)
    verified_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    data_quality_flags: Mapped[dict] = mapped_column(JSON, nullable=True)

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceVerificationHistory().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceVerificationHistory().construct_record_name(self.to_dict())


class G2PRegisterHistoryVerificationHistory(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_verification_history"

    linked_register_mnemonic: Mapped[str] = mapped_column(String, nullable=True)
    update_trigger: Mapped[str] = mapped_column(String, nullable=True)
    data_source: Mapped[str] = mapped_column(String, nullable=True)
    enumerator_id: Mapped[str] = mapped_column(String, nullable=True)
    office_location_code: Mapped[str] = mapped_column(String, nullable=True)
    verification_status: Mapped[str] = mapped_column(String, nullable=True)
    verification_method: Mapped[str] = mapped_column(String, nullable=True)
    verified_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    data_quality_flags: Mapped[dict] = mapped_column(JSON, nullable=True)
