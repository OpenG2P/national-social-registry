from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import ShockTypeEnum


class G2PRegisterSchemaShock(G2PRegisterBaseSchema):
    """
    Schema for Shock.
    link_internal_record_id -> Individual.internal_record_id
    """
    shock_type: Optional[ShockTypeEnum] = None
    shock_date: Optional[date] = None
    shock_period: Optional[str] = None
    coping_strategy: Optional[str] = None


class G2PRegisterHistorySchemaShock(G2PRegisterHistorySchema):
    shock_type: Optional[ShockTypeEnum] = None
    shock_date: Optional[date] = None
    shock_period: Optional[str] = None
    coping_strategy: Optional[str] = None
