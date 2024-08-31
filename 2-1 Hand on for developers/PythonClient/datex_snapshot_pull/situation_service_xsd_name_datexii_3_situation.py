from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from datex_snapshot_pull.situation_service_xsd_name_datexii_3_common import (
    ExtensionType,
    GlobalReference,
    HeaderInformation,
    MultilingualString,
    PayloadPublication,
    Validity,
    VehicleCharacteristics,
    VersionedReference,
    WeatherRelatedRoadConditionTypeEnum2,
)
from datex_snapshot_pull.situation_service_xsd_name_datexii_3_location_referencing import (
    LocationReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/situation"


class AccidentTypeEnum1(Enum):
    ACCIDENT = "accident"
    EXTENDED = "_extended"


class AnimalPresenceTypeEnum1(Enum):
    ANIMALS_ON_THE_ROAD = "animalsOnTheRoad"
    EXTENDED = "_extended"


class CommentTypeEnum1(Enum):
    ABNORMAL_LOAD_MOVEMENT_NOTE = "abnormalLoadMovementNote"
    DATA_PROCESSING_NOTE = "dataProcessingNote"
    DESCRIPTION = "description"
    INTERNAL_NOTE = "internalNote"
    ROADWORKS_NAME = "roadworksName"
    WARNING = "warning"
    OTHER = "other"
    EXTENDED = "_extended"


class ComplianceOptionEnum1(Enum):
    ADVISORY = "advisory"
    MANDATORY = "mandatory"
    EXTENDED = "_extended"


class DrivingConditionTypeEnum1(Enum):
    IMPOSSIBLE = "impossible"
    HAZARDOUS = "hazardous"
    NORMAL = "normal"
    PASSABLE_WITH_CARE = "passableWithCare"
    UNKNOWN = "unknown"
    VERY_HAZARDOUS = "veryHazardous"
    WINTER_CONDITIONS = "winterConditions"
    OTHER = "other"
    EXTENDED = "_extended"


class EnvironmentalObstructionTypeEnum1(Enum):
    AVALANCHES = "avalanches"
    FLOODING = "flooding"
    ROCKFALLS = "rockfalls"
    OTHER = "other"
    EXTENDED = "_extended"


class NonWeatherRelatedRoadConditionTypeEnum1(Enum):
    LOOSE_CHIPPINGS = "looseChippings"
    ROAD_SURFACE_IN_POOR_CONDITION = "roadSurfaceInPoorCondition"
    SLIPPERY_ROAD = "slipperyRoad"
    OTHER = "other"
    EXTENDED = "_extended"


class ObstructionTypeEnum1(Enum):
    OBSTRUCTION_ON_THE_ROAD = "obstructionOnTheRoad"
    SEVERE_FROST_DAMAGED_ROADWAY = "severeFrostDamagedRoadway"
    UNPROTECTED_ACCIDENT_AREA = "unprotectedAccidentArea"
    OTHER = "other"
    EXTENDED = "_extended"


class PoorEnvironmentTypeEnum1(Enum):
    BAD_WEATHER = "badWeather"
    BLIZZARD = "blizzard"
    BLOWING_DUST = "blowingDust"
    BLOWING_SNOW = "blowingSnow"
    FOG = "fog"
    SNOWFALL = "snowfall"
    STORM_FORCE_WINDS = "stormForceWinds"
    STRONG_WINDS = "strongWinds"
    EXTENDED = "_extended"


class ProbabilityOfOccurrenceEnum1(Enum):
    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "riskOf"
    EXTENDED = "_extended"


class RoadMaintenanceTypeEnum1(Enum):
    ROADWORKS = "roadworks"
    SNOWPLOUGHS_IN_USE = "snowploughsInUse"
    OTHER = "other"
    EXTENDED = "_extended"


class RoadOrCarriagewayOrLaneManagementTypeEnum1(Enum):
    CLOSED_PERMANENTLY_FOR_THE_WINTER = "closedPermanentlyForTheWinter"
    ROAD_CLOSED = "roadClosed"
    OTHER = "other"
    EXTENDED = "_extended"


class SeverityEnum1(Enum):
    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"
    NONE = "none"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


@dataclass
class AccidentTypeEnum2:
    class Meta:
        name = "_AccidentTypeEnum"

    value: Optional[AccidentTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class AnimalPresenceTypeEnum2:
    class Meta:
        name = "_AnimalPresenceTypeEnum"

    value: Optional[AnimalPresenceTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class CommentTypeEnum2:
    class Meta:
        name = "_CommentTypeEnum"

    value: Optional[CommentTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class ComplianceOptionEnum2:
    class Meta:
        name = "_ComplianceOptionEnum"

    value: Optional[ComplianceOptionEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class DrivingConditionTypeEnum2:
    class Meta:
        name = "_DrivingConditionTypeEnum"

    value: Optional[DrivingConditionTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class EnvironmentalObstructionTypeEnum2:
    class Meta:
        name = "_EnvironmentalObstructionTypeEnum"

    value: Optional[EnvironmentalObstructionTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class NonWeatherRelatedRoadConditionTypeEnum2:
    class Meta:
        name = "_NonWeatherRelatedRoadConditionTypeEnum"

    value: Optional[NonWeatherRelatedRoadConditionTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class ObstructionTypeEnum2:
    class Meta:
        name = "_ObstructionTypeEnum"

    value: Optional[ObstructionTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class PoorEnvironmentTypeEnum2:
    class Meta:
        name = "_PoorEnvironmentTypeEnum"

    value: Optional[PoorEnvironmentTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class ProbabilityOfOccurrenceEnum2:
    class Meta:
        name = "_ProbabilityOfOccurrenceEnum"

    value: Optional[ProbabilityOfOccurrenceEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class RoadMaintenanceTypeEnum2:
    class Meta:
        name = "_RoadMaintenanceTypeEnum"

    value: Optional[RoadMaintenanceTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class RoadOrCarriagewayOrLaneManagementTypeEnum2:
    class Meta:
        name = "_RoadOrCarriagewayOrLaneManagementTypeEnum"

    value: Optional[RoadOrCarriagewayOrLaneManagementTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class SeverityEnum2:
    class Meta:
        name = "_SeverityEnum"

    value: Optional[SeverityEnum1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        },
    )


@dataclass
class SituationRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_SituationRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="sit:SituationRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Comment:
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    comment_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "commentDateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    comment_type: Optional[CommentTypeEnum2] = field(
        default=None,
        metadata={
            "name": "commentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    comment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_commentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class SituationRecordReference(GlobalReference):
    object_reference: Optional[SituationRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "objectReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    situation_record_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationRecordReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class Cause:
    managed_cause: Optional[SituationRecordReference] = field(
        default=None,
        metadata={
            "name": "managedCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_causeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class SituationRecord:
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum2] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    severity: Optional[SeverityEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    safety_related_message: Optional[bool] = field(
        default=None,
        metadata={
            "name": "safetyRelatedMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    location_reference: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "locationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class OperatorAction(SituationRecord):
    operator_action_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_operatorActionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class Situation:
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    situation_record: List[SituationRecord] = field(
        default_factory=list,
        metadata={
            "name": "situationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        },
    )
    situation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TrafficElement(SituationRecord):
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class Accident(TrafficElement):
    accident_type: List[AccidentTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        },
    )
    accident_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_accidentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class Conditions(TrafficElement):
    driving_condition_type: Optional[DrivingConditionTypeEnum2] = field(
        default=None,
        metadata={
            "name": "drivingConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_conditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class NetworkManagement(OperatorAction):
    compliance_option: Optional[ComplianceOptionEnum2] = field(
        default=None,
        metadata={
            "name": "complianceOption",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    for_vehicles_with_characteristics_of: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_networkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class Obstruction(TrafficElement):
    obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_obstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class Roadworks(OperatorAction):
    roadworks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadworksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class SituationPublication(PayloadPublication):
    situation: List[Situation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
    situation_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class AnimalPresenceObstruction(Obstruction):
    animal_presence_type: Optional[AnimalPresenceTypeEnum2] = field(
        default=None,
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    animal_presence_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_animalPresenceObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class EnvironmentalObstruction(Obstruction):
    environmental_obstruction_type: Optional[
        EnvironmentalObstructionTypeEnum2
    ] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    environmental_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_environmentalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class GeneralObstruction(Obstruction):
    obstruction_type: List[ObstructionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "obstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        },
    )
    general_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_generalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class MaintenanceWorks(Roadworks):
    road_maintenance_type: List[RoadMaintenanceTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "roadMaintenanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        },
    )
    maintenance_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_maintenanceWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class PoorEnvironmentConditions(Conditions):
    poor_environment_type: List[PoorEnvironmentTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        },
    )
    poor_environment_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_poorEnvironmentConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class RoadOrCarriagewayOrLaneManagement(NetworkManagement):
    road_or_carriageway_or_lane_management_type: Optional[
        RoadOrCarriagewayOrLaneManagementTypeEnum2
    ] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "required": True,
        },
    )
    road_or_carriageway_or_lane_management_extension: Optional[
        ExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "_roadOrCarriagewayOrLaneManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class RoadSurfaceConditions(Conditions):
    road_surface_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadSurfaceConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )


@dataclass
class NonWeatherRelatedRoadConditions(RoadSurfaceConditions):
    non_weather_related_road_condition_type: List[
        NonWeatherRelatedRoadConditionTypeEnum2
    ] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        },
    )
    non_weather_related_road_conditions_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "_nonWeatherRelatedRoadConditionsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/situation",
            },
        )
    )


@dataclass
class WeatherRelatedRoadConditions(RoadSurfaceConditions):
    weather_related_road_condition_type: List[
        WeatherRelatedRoadConditionTypeEnum2
    ] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
            "min_occurs": 1,
        },
    )
    weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_weatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/situation",
        },
    )
