from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import AssetTypeEnum


class G2PRegisterSchemaAsset(G2PRegisterBaseSchema):
    """
    Schema for Asset.
    link_internal_record_id -> Household.internal_record_id
    """
    asset_type: Optional[AssetTypeEnum] = None
    asset_category: Optional[str] = None
    quantity: Optional[int] = None
    size_value: Optional[float] = None
    size_unit: Optional[str] = None
    size_band: Optional[str] = None
    details: Optional[dict] = None


class G2PRegisterHistorySchemaAsset(G2PRegisterHistorySchema):
    asset_type: Optional[AssetTypeEnum] = None
    asset_category: Optional[str] = None
    quantity: Optional[int] = None
    size_value: Optional[float] = None
    size_unit: Optional[str] = None
    size_band: Optional[str] = None
    details: Optional[dict] = None
