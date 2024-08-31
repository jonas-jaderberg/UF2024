from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://datex2.eu/schema/3/common"


class ComparisonOperatorEnum1(Enum):
    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL_TO = "greaterThanOrEqualTo"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL_TO = "lessThanOrEqualTo"
    EXTENDED = "_extended"


class ComputationMethodEnum1(Enum):
    ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES = (
        "arithmeticAverageOfSamplesBasedOnAFixedNumberOfSamples"
    )
    ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = (
        "arithmeticAverageOfSamplesInATimePeriod"
    )
    HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = (
        "harmonicAverageOfSamplesInATimePeriod"
    )
    MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD = "medianOfSamplesInATimePeriod"
    MOVING_AVERAGE_OF_SAMPLES = "movingAverageOfSamples"
    EXTENDED = "_extended"


class InformationStatusEnum1(Enum):
    REAL = "real"
    SECURITY_EXERCISE = "securityExercise"
    TECHNICAL_EXERCISE = "technicalExercise"
    TEST = "test"
    EXTENDED = "_extended"


@dataclass
class MultilingualStringValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1024,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Reference:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class ValidityStatusEnum1(Enum):
    ACTIVE = "active"
    PLANNED = "planned"
    SUSPENDED = "suspended"
    DEFINED_BY_VALIDITY_TIME_SPEC = "definedByValidityTimeSpec"
    EXTENDED = "_extended"


@dataclass
class VersionedReference:
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
        },
    )


class WeatherRelatedRoadConditionTypeEnum1(Enum):
    BLACK_ICE = "blackIce"
    ICE = "ice"
    ICY_PATCHES = "icyPatches"
    LOOSE_SNOW = "looseSnow"
    SLIPPERY = "slippery"
    SLUSH_ON_ROAD = "slushOnRoad"
    SNOW = "snow"
    OTHER = "other"
    EXTENDED = "_extended"


class WeightTypeEnum1(Enum):
    ACTUAL = "actual"
    MAXIMUM_PERMITTED = "maximumPermitted"
    EXTENDED = "_extended"


@dataclass
class ExtensionType:
    class Meta:
        name = "_ExtensionType"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class GlobalReference:
    global_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_globalReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )


@dataclass
class InternationalIdentifier:
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
            "max_length": 2,
        },
    )
    national_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "nationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
            "max_length": 1024,
        },
    )
    international_identifier_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )


@dataclass
class MultilingualString:
    values: Optional["MultilingualString.Values"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )

    @dataclass
    class Values:
        value: List[MultilingualStringValue] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/common",
                "min_occurs": 1,
            },
        )


@dataclass
class OverallPeriod:
    overall_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    overall_end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallEndTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )
    overall_period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_overallPeriodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )


@dataclass
class ComparisonOperatorEnum2:
    class Meta:
        name = "_ComparisonOperatorEnum"

    value: Optional[ComparisonOperatorEnum1] = field(
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
class ComputationMethodEnum2:
    class Meta:
        name = "_ComputationMethodEnum"

    value: Optional[ComputationMethodEnum1] = field(
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
class InformationStatusEnum2:
    class Meta:
        name = "_InformationStatusEnum"

    value: Optional[InformationStatusEnum1] = field(
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
class ValidityStatusEnum2:
    class Meta:
        name = "_ValidityStatusEnum"

    value: Optional[ValidityStatusEnum1] = field(
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
class WeatherRelatedRoadConditionTypeEnum2:
    class Meta:
        name = "_WeatherRelatedRoadConditionTypeEnum"

    value: Optional[WeatherRelatedRoadConditionTypeEnum1] = field(
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
class WeightTypeEnum2:
    class Meta:
        name = "_WeightTypeEnum"

    value: Optional[WeightTypeEnum1] = field(
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
class DataValue:
    data_error: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dataError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )
    reason_for_data_error: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForDataError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )
    data_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_dataValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    computational_method: Optional[ComputationMethodEnum1] = field(
        default=None,
        metadata={
            "name": "computationalMethod",
            "type": "Attribute",
        },
    )
    number_of_incomplete_inputs: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIncompleteInputs",
            "type": "Attribute",
        },
    )
    number_of_input_values_used: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfInputValuesUsed",
            "type": "Attribute",
        },
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Attribute",
        },
    )
    standard_deviation: Optional[float] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Attribute",
        },
    )
    supplier_calculated_data_quality: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplierCalculatedDataQuality",
            "type": "Attribute",
        },
    )


@dataclass
class GrossWeightCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum2] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    gross_vehicle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "grossVehicleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    type_of_weight: Optional[WeightTypeEnum2] = field(
        default=None,
        metadata={
            "name": "typeOfWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    gross_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_grossWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )


@dataclass
class HeaderInformation:
    information_status: Optional[InformationStatusEnum2] = field(
        default=None,
        metadata={
            "name": "informationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    header_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_headerInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )


@dataclass
class PayloadPublication:
    feed_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "feedType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        },
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    publication_creator: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "publicationCreator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    payload_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_payloadPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    model_base_version: str = field(
        init=False,
        default="3",
        metadata={
            "name": "modelBaseVersion",
            "type": "Attribute",
            "required": True,
        },
    )
    extension_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "extensionName",
            "type": "Attribute",
        },
    )
    extension_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "extensionVersion",
            "type": "Attribute",
        },
    )
    profile_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "profileName",
            "type": "Attribute",
        },
    )
    profile_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "profileVersion",
            "type": "Attribute",
        },
    )


@dataclass
class Validity:
    validity_status: Optional[ValidityStatusEnum2] = field(
        default=None,
        metadata={
            "name": "validityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        },
    )
    validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_validityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )


@dataclass
class VehicleCharacteristics:
    gross_weight_characteristic: List[GrossWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "grossWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 2,
        },
    )
    vehicle_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vehicleCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        },
    )
