from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from ..models.enums import (
    GrievanceStatusEnum,
    GrievanceTypeEnum,
    ResolutionCodeEnum,
    SubmissionChannelEnum,
)


class G2PRegisterSchemaGrievance(G2PRegisterBaseSchema):
    """
    Schema for Grievance.
    link_internal_record_id -> Individual.internal_record_id
    """
    grievance_case_id: Optional[str] = None
    grievance_type: Optional[GrievanceTypeEnum] = None
    submission_channel: Optional[SubmissionChannelEnum] = None
    grievance_status: Optional[GrievanceStatusEnum] = None
    submission_date: Optional[date] = None
    resolution_date: Optional[date] = None
    resolution_code: Optional[ResolutionCodeEnum] = None
    resolution_rationale: Optional[str] = None
    protection_referral_flag: Optional[bool] = None


class G2PRegisterHistorySchemaGrievance(G2PRegisterHistorySchema):
    grievance_case_id: Optional[str] = None
    grievance_type: Optional[GrievanceTypeEnum] = None
    submission_channel: Optional[SubmissionChannelEnum] = None
    grievance_status: Optional[GrievanceStatusEnum] = None
    submission_date: Optional[date] = None
    resolution_date: Optional[date] = None
    resolution_code: Optional[ResolutionCodeEnum] = None
    resolution_rationale: Optional[str] = None
    protection_referral_flag: Optional[bool] = None
