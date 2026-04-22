from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceIndividualDisability
from .enums import DisabilityDomainEnum, DisabilitySeverityEnum


# All Register classes should have the prefix G2PRegister
class G2PRegisterIndividualDisability(G2PRegister):
    __tablename__ = "g2p_register_individual_disabilities"

    # link_internal_record_id -> Individual.internal_record_id
    #
    # One row per functional-difficulty domain the individual has been assessed
    # in. The Washington Group Short Set has six domains, and an individual may
    # have different severities across them, so the severity lives per-row
    # (not on the Individual record). The high-level YES/NO/UNKNOWN summary
    # stays on Individual.disability_status.
    disability_domain: Mapped[DisabilityDomainEnum] = mapped_column(String, nullable=True, index=True)
    disability_severity: Mapped[DisabilitySeverityEnum] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceIndividualDisability().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceIndividualDisability().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryIndividualDisability(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_individual_disabilities"

    disability_domain: Mapped[str] = mapped_column(String, nullable=True)
    disability_severity: Mapped[str] = mapped_column(String, nullable=True)
