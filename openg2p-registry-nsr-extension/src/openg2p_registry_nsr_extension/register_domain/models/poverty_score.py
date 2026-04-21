from sqlalchemy import JSON, Date, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServicePovertyScore
from .enums import PmtScoreTypeEnum


class G2PRegisterPovertyScore(G2PRegister):
    __tablename__ = "g2p_register_poverty_scores"

    # link_internal_record_id -> Household.internal_record_id
    pmt_score: Mapped[float] = mapped_column(Numeric, nullable=True)
    pmt_score_type: Mapped[PmtScoreTypeEnum] = mapped_column(String, nullable=True)
    pmt_variables: Mapped[dict] = mapped_column(JSON, nullable=True)
    pmt_calculation_date: Mapped[Date] = mapped_column(Date, nullable=True)
    pmt_model_version: Mapped[str] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServicePovertyScore().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServicePovertyScore().construct_record_name(self.to_dict())


class G2PRegisterHistoryPovertyScore(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_poverty_scores"

    pmt_score: Mapped[float] = mapped_column(Numeric, nullable=True)
    pmt_score_type: Mapped[str] = mapped_column(String, nullable=True)
    pmt_variables: Mapped[dict] = mapped_column(JSON, nullable=True)
    pmt_calculation_date: Mapped[Date] = mapped_column(Date, nullable=True)
    pmt_model_version: Mapped[str] = mapped_column(String, nullable=True)
