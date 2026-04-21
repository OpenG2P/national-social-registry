import enum


# ---------------------------------------------------------------------------
# Individual – identity, demographics, relationships
# ---------------------------------------------------------------------------

class AgeMethodEnum(str, enum.Enum):
    DOCUMENTED = "DOCUMENTED"
    ESTIMATED = "ESTIMATED"


class CitizenshipCategoryEnum(str, enum.Enum):
    CITIZEN = "CITIZEN"
    REFUGEE = "REFUGEE"
    IDP = "IDP"
    RETURNEE = "RETURNEE"
    RESIDENT = "RESIDENT"


class ResidencyStatusEnum(str, enum.Enum):
    USUAL_MEMBER = "USUAL_MEMBER"
    TEMPORARY = "TEMPORARY"
    ABSENT = "ABSENT"


class RelationshipToHeadEnum(str, enum.Enum):
    SELF = "SELF"
    SPOUSE = "SPOUSE"
    CHILD = "CHILD"
    PARENT = "PARENT"
    SIBLING = "SIBLING"
    OTHER_RELATIVE = "OTHER_RELATIVE"
    NON_RELATIVE = "NON_RELATIVE"


class IdentityEvidenceTypeEnum(str, enum.Enum):
    FOUNDATIONAL_ID_VERIFIED = "FOUNDATIONAL_ID_VERIFIED"
    DOCUMENT = "DOCUMENT"
    NONE = "NONE"
    EXCEPTION = "EXCEPTION"


class VerificationStatusEnum(str, enum.Enum):
    VERIFIED = "VERIFIED"
    PENDING = "PENDING"
    FAILED = "FAILED"
    EXCEPTION = "EXCEPTION"


class PreferredContactMethodEnum(str, enum.Enum):
    CALL = "CALL"
    SMS = "SMS"
    VIA_LOCAL_OFFICE = "VIA_LOCAL_OFFICE"
    NONE = "NONE"


# ---------------------------------------------------------------------------
# Individual – vulnerability and inclusion
# ---------------------------------------------------------------------------

class DisabilityStatusEnum(str, enum.Enum):
    YES = "YES"
    NO = "NO"
    UNKNOWN = "UNKNOWN"


class DisabilitySeverityEnum(str, enum.Enum):
    NO_DIFFICULTY = "NO_DIFFICULTY"
    SOME_DIFFICULTY = "SOME_DIFFICULTY"
    A_LOT_OF_DIFFICULTY = "A_LOT_OF_DIFFICULTY"
    CANNOT_DO_AT_ALL = "CANNOT_DO_AT_ALL"


class DisplacementStatusEnum(str, enum.Enum):
    HOST_COMMUNITY = "HOST_COMMUNITY"
    IDP = "IDP"
    RETURNEE = "RETURNEE"
    REFUGEE = "REFUGEE"


class PastoralistClassificationEnum(str, enum.Enum):
    PASTORALIST = "PASTORALIST"
    SEMI_PASTORALIST = "SEMI_PASTORALIST"
    SETTLED = "SETTLED"


class EmploymentStatusEnum(str, enum.Enum):
    EMPLOYED = "EMPLOYED"
    SELF_EMPLOYED = "SELF_EMPLOYED"
    UNEMPLOYED = "UNEMPLOYED"
    STUDENT = "STUDENT"
    RETIRED = "RETIRED"
    OTHER = "OTHER"


# ---------------------------------------------------------------------------
# Household – composition, dwelling, services
# ---------------------------------------------------------------------------

class HeadshipTypeEnum(str, enum.Enum):
    MALE_HEADED = "MALE_HEADED"
    FEMALE_HEADED = "FEMALE_HEADED"
    CHILD_HEADED = "CHILD_HEADED"
    ELDERLY_HEADED = "ELDERLY_HEADED"
    DISABLED_HEADED = "DISABLED_HEADED"


class DwellingTypeEnum(str, enum.Enum):
    PERMANENT = "PERMANENT"
    SEMI_PERMANENT = "SEMI_PERMANENT"
    TEMPORARY = "TEMPORARY"


class TenureStatusEnum(str, enum.Enum):
    OWNED = "OWNED"
    RENTED = "RENTED"
    HOSTED = "HOSTED"
    TEMPORARY = "TEMPORARY"


class WaterSourceTypeEnum(str, enum.Enum):
    PIPED = "PIPED"
    PUBLIC_TAP = "PUBLIC_TAP"
    WELL = "WELL"
    SPRING = "SPRING"
    SURFACE_WATER = "SURFACE_WATER"
    RAINWATER = "RAINWATER"
    TANKER_TRUCK = "TANKER_TRUCK"
    OTHER = "OTHER"


class SanitationTypeEnum(str, enum.Enum):
    FLUSH_TOILET = "FLUSH_TOILET"
    PIT_LATRINE = "PIT_LATRINE"
    COMPOSTING_TOILET = "COMPOSTING_TOILET"
    SHARED = "SHARED"
    OPEN = "OPEN"
    OTHER = "OTHER"


class LightingSourceEnum(str, enum.Enum):
    GRID = "GRID"
    SOLAR = "SOLAR"
    GENERATOR = "GENERATOR"
    KEROSENE = "KEROSENE"
    CANDLE = "CANDLE"
    NONE = "NONE"


class CookingFuelEnum(str, enum.Enum):
    ELECTRICITY = "ELECTRICITY"
    GAS = "GAS"
    KEROSENE = "KEROSENE"
    CHARCOAL = "CHARCOAL"
    FIREWOOD = "FIREWOOD"
    BIOMASS = "BIOMASS"
    OTHER = "OTHER"


class MobilePhoneTypeEnum(str, enum.Enum):
    NONE = "NONE"
    BASIC = "BASIC"
    SMARTPHONE = "SMARTPHONE"


# ---------------------------------------------------------------------------
# Asset
# ---------------------------------------------------------------------------

class AssetTypeEnum(str, enum.Enum):
    LAND = "LAND"
    LIVESTOCK = "LIVESTOCK"
    PRODUCTIVE_TOOL = "PRODUCTIVE_TOOL"
    CONSUMER_DURABLE = "CONSUMER_DURABLE"
    VEHICLE = "VEHICLE"
    OTHER = "OTHER"


# ---------------------------------------------------------------------------
# Shock
# ---------------------------------------------------------------------------

class ShockTypeEnum(str, enum.Enum):
    DROUGHT = "DROUGHT"
    FLOOD = "FLOOD"
    CONFLICT = "CONFLICT"
    ILLNESS = "ILLNESS"
    DEATH_OF_EARNER = "DEATH_OF_EARNER"
    JOB_LOSS = "JOB_LOSS"
    PRICE_SHOCK = "PRICE_SHOCK"
    CROP_FAILURE = "CROP_FAILURE"
    LIVESTOCK_LOSS = "LIVESTOCK_LOSS"
    FIRE = "FIRE"
    OTHER = "OTHER"


# ---------------------------------------------------------------------------
# Consent
# ---------------------------------------------------------------------------

class ConsentMethodEnum(str, enum.Enum):
    SIGNED = "SIGNED"
    VERBAL = "VERBAL"
    DIGITAL = "DIGITAL"
    BIOMETRIC = "BIOMETRIC"


# ---------------------------------------------------------------------------
# Grievance
# ---------------------------------------------------------------------------

class GrievanceTypeEnum(str, enum.Enum):
    EXCLUSION = "EXCLUSION"
    INCLUSION = "INCLUSION"
    DATA_ERROR = "DATA_ERROR"
    PAYMENT = "PAYMENT"
    PROTECTION = "PROTECTION"
    OTHER = "OTHER"


class SubmissionChannelEnum(str, enum.Enum):
    IN_PERSON = "IN_PERSON"
    PHONE = "PHONE"
    USSD = "USSD"
    COMMUNITY_COMMITTEE = "COMMUNITY_COMMITTEE"
    ONLINE = "ONLINE"


class GrievanceStatusEnum(str, enum.Enum):
    OPEN = "OPEN"
    UNDER_REVIEW = "UNDER_REVIEW"
    RESOLVED = "RESOLVED"
    APPEALED = "APPEALED"
    CLOSED = "CLOSED"


class ResolutionCodeEnum(str, enum.Enum):
    ADDED = "ADDED"
    CORRECTED = "CORRECTED"
    REFERRED = "REFERRED"
    REJECTED = "REJECTED"


# ---------------------------------------------------------------------------
# Verification history / update audit
# ---------------------------------------------------------------------------

class UpdateTriggerEnum(str, enum.Enum):
    ON_DEMAND = "ON_DEMAND"
    RECERTIFICATION = "RECERTIFICATION"
    LIFE_EVENT = "LIFE_EVENT"
    SHOCK = "SHOCK"
    INTEGRATION_SYNC = "INTEGRATION_SYNC"


class VerificationMethodEnum(str, enum.Enum):
    PHONE_CALL = "PHONE_CALL"
    FIELD_VISIT = "FIELD_VISIT"
    DOCUMENT_CHECK = "DOCUMENT_CHECK"
    API = "API"
    NONE = "NONE"


class RecordVerificationStatusEnum(str, enum.Enum):
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    SPOT_CHECKED = "SPOT_CHECKED"


# ---------------------------------------------------------------------------
# Poverty score
# ---------------------------------------------------------------------------

class PmtScoreTypeEnum(str, enum.Enum):
    PMT = "PMT"
    MPI = "MPI"
    PPI = "PPI"
    CUSTOM = "CUSTOM"


# ---------------------------------------------------------------------------
# Program participation
# ---------------------------------------------------------------------------

class PaymentChannelPreferenceEnum(str, enum.Enum):
    BANK = "BANK"
    MOBILE_MONEY = "MOBILE_MONEY"
    CASH = "CASH"
    OTHER = "OTHER"


class PaymentVerificationStatusEnum(str, enum.Enum):
    VERIFIED = "VERIFIED"
    PENDING = "PENDING"
    FAILED = "FAILED"


# ---------------------------------------------------------------------------
# Shared – parent type for tables that can link to either register
# ---------------------------------------------------------------------------

class LinkedRegisterMnemonicEnum(str, enum.Enum):
    INDIVIDUAL = "Individual"
    HOUSEHOLD = "Household"
