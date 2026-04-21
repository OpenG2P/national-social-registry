from sqlalchemy import Date, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceShock
from .enums import ShockTypeEnum


class G2PRegisterShock(G2PRegister):
    __tablename__ = "g2p_register_shocks"

    # link_internal_record_id -> Individual.internal_record_id
    shock_type: Mapped[ShockTypeEnum] = mapped_column(String, nullable=True)
    shock_date: Mapped[Date] = mapped_column(Date, nullable=True, index=True)   # time-based analytics / shock-response queries
    shock_period: Mapped[str] = mapped_column(String, nullable=True)            # e.g., "2026-Q1"
    coping_strategy: Mapped[str] = mapped_column(String, nullable=True)         # attribute lookup

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceShock().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceShock().construct_record_name(self.to_dict())


class G2PRegisterHistoryShock(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_shocks"

    shock_type: Mapped[str] = mapped_column(String, nullable=True)
    shock_date: Mapped[Date] = mapped_column(Date, nullable=True)
    shock_period: Mapped[str] = mapped_column(String, nullable=True)
    coping_strategy: Mapped[str] = mapped_column(String, nullable=True)
