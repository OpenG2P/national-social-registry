from sqlalchemy import JSON, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceAsset
from .enums import AssetTypeEnum


class G2PRegisterAsset(G2PRegister):
    __tablename__ = "g2p_register_assets"

    # link_internal_record_id -> Household.internal_record_id
    asset_type: Mapped[AssetTypeEnum] = mapped_column(String, nullable=True)
    asset_category: Mapped[str] = mapped_column(String, nullable=True)   # attribute lookup, varies by asset_type
    quantity: Mapped[int] = mapped_column(Integer, nullable=True)
    size_value: Mapped[float] = mapped_column(Numeric, nullable=True)
    size_unit: Mapped[str] = mapped_column(String, nullable=True)
    size_band: Mapped[str] = mapped_column(String, nullable=True)        # e.g., "0-1ha", "1-5 heads"
    details: Mapped[dict] = mapped_column(JSON, nullable=True)           # free-form per-type attributes

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceAsset().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceAsset().construct_record_name(self.to_dict())


class G2PRegisterHistoryAsset(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_assets"

    asset_type: Mapped[str] = mapped_column(String, nullable=True)
    asset_category: Mapped[str] = mapped_column(String, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=True)
    size_value: Mapped[float] = mapped_column(Numeric, nullable=True)
    size_unit: Mapped[str] = mapped_column(String, nullable=True)
    size_band: Mapped[str] = mapped_column(String, nullable=True)
    details: Mapped[dict] = mapped_column(JSON, nullable=True)
