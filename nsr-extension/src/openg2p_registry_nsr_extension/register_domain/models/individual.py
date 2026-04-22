from sqlalchemy import JSON, Boolean, Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PPerson,
    G2PPersonHistory, G2PGeoHistory
)
from ..services import G2PRegisterDomainServiceIndividual
from .enums import (
    AgeMethodEnum,
    CitizenshipCategoryEnum,
    DisabilityStatusEnum,
    DisplacementStatusEnum,
    EmploymentStatusEnum,
    IdentityEvidenceTypeEnum,
    PastoralistClassificationEnum,
    PreferredContactMethodEnum,
    RelationshipToHeadEnum,
    ResidencyStatusEnum,
    VerificationStatusEnum,
)


# All Register classes should have the prefix G2PRegister
class G2PRegisterIndividual(G2PRegister, G2PPerson, G2PGeo):
    __tablename__ = "g2p_register_individuals"

    # Identity
    # foundational_id is provided by G2PPerson
    foundational_id_masked: Mapped[str] = mapped_column(String, nullable=True)
    foundational_id_verification_status: Mapped[VerificationStatusEnum] = mapped_column(String, nullable=True)
    identity_evidence_type: Mapped[IdentityEvidenceTypeEnum] = mapped_column(String, nullable=True)
    legacy_program_ids: Mapped[dict] = mapped_column(JSON, nullable=True)  # map of legacy system -> id

    # Names — kept alongside G2PPerson's first/middle/last for search & dedup
    # on populations with inconsistent transliteration or single-name cultures.
    full_name: Mapped[str] = mapped_column(String, nullable=True, index=True)
    alias_names: Mapped[list] = mapped_column(JSON, nullable=True)  # alternative spellings / known-as list

    # Demographics (beyond G2PPerson)
    estimated_age: Mapped[int] = mapped_column(Integer, nullable=True)
    age_method: Mapped[AgeMethodEnum] = mapped_column(String, nullable=True)
    citizenship_category: Mapped[CitizenshipCategoryEnum] = mapped_column(String, nullable=True)

    # Household membership (Individual → Household via link_internal_record_id)
    relationship_to_head: Mapped[RelationshipToHeadEnum] = mapped_column(String, nullable=True)
    residency_status: Mapped[ResidencyStatusEnum] = mapped_column(String, nullable=True)
    dependency_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # Contact
    preferred_contact_method: Mapped[PreferredContactMethodEnum] = mapped_column(String, nullable=True)
    contact_person_name: Mapped[str] = mapped_column(String, nullable=True)

    # Vulnerability and inclusion
    # `disability_status` is the high-level YES/NO/UNKNOWN flag. Per-domain
    # severities live in the separate IndividualDisability table (multi-row),
    # since one person can have functional difficulty in multiple WG domains
    # with different severities.
    disability_status: Mapped[DisabilityStatusEnum] = mapped_column(String, nullable=True)
    plw_status: Mapped[bool] = mapped_column(Boolean, nullable=True)       # pregnant/lactating
    plw_status_date: Mapped[Date] = mapped_column(Date, nullable=True)
    orphanhood_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    chronic_illness_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    displacement_status: Mapped[DisplacementStatusEnum] = mapped_column(String, nullable=True)
    pastoralist_classification: Mapped[PastoralistClassificationEnum] = mapped_column(String, nullable=True)
    high_mobility_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # Livelihoods (single primary/secondary kept inline; shocks go to a table)
    primary_livelihood: Mapped[str] = mapped_column(String, nullable=True)       # attribute lookup (ISCO-aligned)
    secondary_livelihood: Mapped[str] = mapped_column(String, nullable=True)     # attribute lookup
    employment_status: Mapped[EmploymentStatusEnum] = mapped_column(String, nullable=True)
    coping_strategies_index: Mapped[int] = mapped_column(Integer, nullable=True)

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceIndividual().construct_record_name(self.to_dict())

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceIndividual().construct_search_text(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryIndividual(G2PRegisterHistory, G2PPersonHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_individuals"

    foundational_id_masked: Mapped[str] = mapped_column(String, nullable=True)
    foundational_id_verification_status: Mapped[str] = mapped_column(String, nullable=True)
    identity_evidence_type: Mapped[str] = mapped_column(String, nullable=True)
    legacy_program_ids: Mapped[dict] = mapped_column(JSON, nullable=True)

    full_name: Mapped[str] = mapped_column(String, nullable=True)
    alias_names: Mapped[list] = mapped_column(JSON, nullable=True)

    estimated_age: Mapped[int] = mapped_column(Integer, nullable=True)
    age_method: Mapped[str] = mapped_column(String, nullable=True)
    citizenship_category: Mapped[str] = mapped_column(String, nullable=True)

    relationship_to_head: Mapped[str] = mapped_column(String, nullable=True)
    residency_status: Mapped[str] = mapped_column(String, nullable=True)
    dependency_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)

    preferred_contact_method: Mapped[str] = mapped_column(String, nullable=True)
    contact_person_name: Mapped[str] = mapped_column(String, nullable=True)

    disability_status: Mapped[str] = mapped_column(String, nullable=True)
    plw_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
    plw_status_date: Mapped[Date] = mapped_column(Date, nullable=True)
    orphanhood_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    chronic_illness_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    displacement_status: Mapped[str] = mapped_column(String, nullable=True)
    pastoralist_classification: Mapped[str] = mapped_column(String, nullable=True)
    high_mobility_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)

    primary_livelihood: Mapped[str] = mapped_column(String, nullable=True)
    secondary_livelihood: Mapped[str] = mapped_column(String, nullable=True)
    employment_status: Mapped[str] = mapped_column(String, nullable=True)
    coping_strategies_index: Mapped[int] = mapped_column(Integer, nullable=True)
