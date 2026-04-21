from sqlalchemy import JSON, Boolean, Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceConsent
from .enums import ConsentMethodEnum


class G2PRegisterConsent(G2PRegister):
    __tablename__ = "g2p_register_consents"

    # link_internal_record_id -> Individual.internal_record_id
    consent_captured: Mapped[bool] = mapped_column(Boolean, nullable=True)
    consent_date: Mapped[Date] = mapped_column(Date, nullable=True, index=True)   # "latest consent per individual" lookups
    consent_scope: Mapped[dict] = mapped_column(JSON, nullable=True)              # list of purpose/institution codes
    consent_method: Mapped[ConsentMethodEnum] = mapped_column(String, nullable=True)
    consent_evidence_ref: Mapped[str] = mapped_column(Text, nullable=True)        # document storage reference
    data_sharing_restrictions: Mapped[dict] = mapped_column(JSON, nullable=True)

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceConsent().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceConsent().construct_record_name(self.to_dict())


class G2PRegisterHistoryConsent(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_consents"

    consent_captured: Mapped[bool] = mapped_column(Boolean, nullable=True)
    consent_date: Mapped[Date] = mapped_column(Date, nullable=True)
    consent_scope: Mapped[dict] = mapped_column(JSON, nullable=True)
    consent_method: Mapped[str] = mapped_column(String, nullable=True)
    consent_evidence_ref: Mapped[str] = mapped_column(Text, nullable=True)
    data_sharing_restrictions: Mapped[dict] = mapped_column(JSON, nullable=True)
