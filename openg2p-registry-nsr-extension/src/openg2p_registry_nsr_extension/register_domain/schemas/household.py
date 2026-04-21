from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PGeoSchema,
    G2PRegisterHistorySchema, G2PGeoHistorySchema
)
from ..models.enums import (
    CookingFuelEnum,
    DwellingTypeEnum,
    HeadshipTypeEnum,
    LightingSourceEnum,
    MobilePhoneTypeEnum,
    SanitationTypeEnum,
    TenureStatusEnum,
    WaterSourceTypeEnum,
)


class G2PRegisterSchemaHousehold(G2PRegisterBaseSchema, G2PGeoSchema):
    """
    Schema for Household register.
    Inherits fields from G2PRegisterBaseSchema and G2PGeoSchema.
    """
    household_head_internal_record_id: Optional[str] = None
    household_head_name: Optional[str] = None
    headship_type: Optional[HeadshipTypeEnum] = None

    size_total: Optional[int] = None
    size_adults: Optional[int] = None
    size_children_u5: Optional[int] = None
    size_school_age: Optional[int] = None
    size_elderly: Optional[int] = None
    number_of_female_members: Optional[int] = None
    number_of_male_members: Optional[int] = None
    elderly_member_present: Optional[bool] = None

    dwelling_type: Optional[DwellingTypeEnum] = None
    roof_material: Optional[str] = None
    wall_material: Optional[str] = None
    floor_material: Optional[str] = None
    tenure_status: Optional[TenureStatusEnum] = None
    rooms_count: Optional[int] = None
    overcrowding_indicator: Optional[float] = None

    water_source_type: Optional[WaterSourceTypeEnum] = None
    water_distance_minutes: Optional[int] = None
    sanitation_type: Optional[SanitationTypeEnum] = None
    lighting_source: Optional[LightingSourceEnum] = None
    cooking_fuel_type: Optional[CookingFuelEnum] = None
    mobile_phone_type: Optional[MobilePhoneTypeEnum] = None


class G2PRegisterHistorySchemaHousehold(G2PRegisterHistorySchema, G2PGeoHistorySchema):
    household_head_internal_record_id: Optional[str] = None
    household_head_name: Optional[str] = None
    headship_type: Optional[HeadshipTypeEnum] = None

    size_total: Optional[int] = None
    size_adults: Optional[int] = None
    size_children_u5: Optional[int] = None
    size_school_age: Optional[int] = None
    size_elderly: Optional[int] = None
    number_of_female_members: Optional[int] = None
    number_of_male_members: Optional[int] = None
    elderly_member_present: Optional[bool] = None

    dwelling_type: Optional[DwellingTypeEnum] = None
    roof_material: Optional[str] = None
    wall_material: Optional[str] = None
    floor_material: Optional[str] = None
    tenure_status: Optional[TenureStatusEnum] = None
    rooms_count: Optional[int] = None
    overcrowding_indicator: Optional[float] = None

    water_source_type: Optional[WaterSourceTypeEnum] = None
    water_distance_minutes: Optional[int] = None
    sanitation_type: Optional[SanitationTypeEnum] = None
    lighting_source: Optional[LightingSourceEnum] = None
    cooking_fuel_type: Optional[CookingFuelEnum] = None
    mobile_phone_type: Optional[MobilePhoneTypeEnum] = None
