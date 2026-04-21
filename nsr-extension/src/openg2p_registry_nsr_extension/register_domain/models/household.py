from sqlalchemy import Boolean, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoHistory
from ..services import G2PRegisterDomainServiceHousehold
from .enums import (
    CookingFuelEnum,
    DwellingTypeEnum,
    HeadshipTypeEnum,
    LightingSourceEnum,
    MobilePhoneTypeEnum,
    SanitationTypeEnum,
    TenureStatusEnum,
    WaterSourceTypeEnum,
)


# All Register classes should have the prefix G2PRegister
class G2PRegisterHousehold(G2PRegister, G2PGeo):
    __tablename__ = "g2p_register_households"

    # Composition and headship
    household_head_internal_record_id: Mapped[str] = mapped_column(String, nullable=True)  # → Individual.internal_record_id
    household_head_name: Mapped[str] = mapped_column(String, nullable=True)
    headship_type: Mapped[HeadshipTypeEnum] = mapped_column(String, nullable=True)

    size_total: Mapped[int] = mapped_column(Integer, nullable=True)
    size_adults: Mapped[int] = mapped_column(Integer, nullable=True)
    size_children_u5: Mapped[int] = mapped_column(Integer, nullable=True)
    size_school_age: Mapped[int] = mapped_column(Integer, nullable=True)
    size_elderly: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_female_members: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_male_members: Mapped[int] = mapped_column(Integer, nullable=True)
    elderly_member_present: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # Dwelling
    dwelling_type: Mapped[DwellingTypeEnum] = mapped_column(String, nullable=True)
    roof_material: Mapped[str] = mapped_column(String, nullable=True)
    wall_material: Mapped[str] = mapped_column(String, nullable=True)
    floor_material: Mapped[str] = mapped_column(String, nullable=True)
    tenure_status: Mapped[TenureStatusEnum] = mapped_column(String, nullable=True)
    rooms_count: Mapped[int] = mapped_column(Integer, nullable=True)
    overcrowding_indicator: Mapped[float] = mapped_column(Numeric, nullable=True)

    # Basic services
    water_source_type: Mapped[WaterSourceTypeEnum] = mapped_column(String, nullable=True)
    water_distance_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    sanitation_type: Mapped[SanitationTypeEnum] = mapped_column(String, nullable=True)
    lighting_source: Mapped[LightingSourceEnum] = mapped_column(String, nullable=True)
    cooking_fuel_type: Mapped[CookingFuelEnum] = mapped_column(String, nullable=True)
    mobile_phone_type: Mapped[MobilePhoneTypeEnum] = mapped_column(String, nullable=True)

    def get_search_text_fields(self) -> str:
        return G2PRegisterDomainServiceHousehold().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        return G2PRegisterDomainServiceHousehold().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHousehold(G2PRegisterHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_households"

    household_head_internal_record_id: Mapped[str] = mapped_column(String, nullable=True)
    household_head_name: Mapped[str] = mapped_column(String, nullable=True)
    headship_type: Mapped[str] = mapped_column(String, nullable=True)

    size_total: Mapped[int] = mapped_column(Integer, nullable=True)
    size_adults: Mapped[int] = mapped_column(Integer, nullable=True)
    size_children_u5: Mapped[int] = mapped_column(Integer, nullable=True)
    size_school_age: Mapped[int] = mapped_column(Integer, nullable=True)
    size_elderly: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_female_members: Mapped[int] = mapped_column(Integer, nullable=True)
    number_of_male_members: Mapped[int] = mapped_column(Integer, nullable=True)
    elderly_member_present: Mapped[bool] = mapped_column(Boolean, nullable=True)

    dwelling_type: Mapped[str] = mapped_column(String, nullable=True)
    roof_material: Mapped[str] = mapped_column(String, nullable=True)
    wall_material: Mapped[str] = mapped_column(String, nullable=True)
    floor_material: Mapped[str] = mapped_column(String, nullable=True)
    tenure_status: Mapped[str] = mapped_column(String, nullable=True)
    rooms_count: Mapped[int] = mapped_column(Integer, nullable=True)
    overcrowding_indicator: Mapped[float] = mapped_column(Numeric, nullable=True)

    water_source_type: Mapped[str] = mapped_column(String, nullable=True)
    water_distance_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    sanitation_type: Mapped[str] = mapped_column(String, nullable=True)
    lighting_source: Mapped[str] = mapped_column(String, nullable=True)
    cooking_fuel_type: Mapped[str] = mapped_column(String, nullable=True)
    mobile_phone_type: Mapped[str] = mapped_column(String, nullable=True)
