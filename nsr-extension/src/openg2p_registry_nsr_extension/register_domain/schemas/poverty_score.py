from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import PmtScoreTypeEnum


class G2PRegisterSchemaPovertyScore(G2PRegisterBaseSchema):
    """
    Schema for Poverty Score register.
    link_internal_record_id -> Household.internal_record_id
    """
    pmt_score: Optional[float] = None
    pmt_score_type: Optional[PmtScoreTypeEnum] = None
    pmt_variables: Optional[dict] = None
    pmt_calculation_date: Optional[date] = None
    pmt_model_version: Optional[str] = None


class G2PRegisterHistorySchemaPovertyScore(G2PRegisterHistorySchema):
    pmt_score: Optional[float] = None
    pmt_score_type: Optional[PmtScoreTypeEnum] = None
    pmt_variables: Optional[dict] = None
    pmt_calculation_date: Optional[date] = None
    pmt_model_version: Optional[str] = None
