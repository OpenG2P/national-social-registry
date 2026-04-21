from sqlalchemy import Boolean, Date, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from ..services import G2PRegisterDomainServiceGrievance
from .enums import (
    GrievanceStatusEnum,
    GrievanceTypeEnum,
    ResolutionCodeEnum,
    SubmissionChannelEnum,
)


class G2PRegisterGrievance(G2PRegister):
    __tablename__ = "g2p_register_grievances"

    # link_internal_record_id -> Individual.internal_record_id
    grievance_case_id: Mapped[str] = mapped_column(String, nullable=True)
    grievance_type: Mapped[GrievanceTypeEnum] = mapped_column(String, nullable=True)
    submission_channel: Mapped[SubmissionChannelEnum] = mapped_column(String, nullable=True)
    grievance_status: Mapped[GrievanceStatusEnum] = mapped_column(String, nullable=True)
    submission_date: Mapped[Date] = mapped_column(Date, nullable=True)
    resolution_date: Mapped[Date] = mapped_column(Date, nullable=True)
    resolution_code: Mapped[ResolutionCodeEnum] = mapped_column(String, nullable=True)
    resolution_rationale: Mapped[str] = mapped_column(String, nullable=True)  # attribute lookup
    protection_referral_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceGrievance().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceGrievance().construct_record_name(self.to_dict())


class G2PRegisterHistoryGrievance(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_grievances"

    grievance_case_id: Mapped[str] = mapped_column(String, nullable=True)
    grievance_type: Mapped[str] = mapped_column(String, nullable=True)
    submission_channel: Mapped[str] = mapped_column(String, nullable=True)
    grievance_status: Mapped[str] = mapped_column(String, nullable=True)
    submission_date: Mapped[Date] = mapped_column(Date, nullable=True)
    resolution_date: Mapped[Date] = mapped_column(Date, nullable=True)
    resolution_code: Mapped[str] = mapped_column(String, nullable=True)
    resolution_rationale: Mapped[str] = mapped_column(String, nullable=True)
    protection_referral_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
