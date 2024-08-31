from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from datex_snapshot_pull.situation_service_xsd_name_datexii_3_common import (
    ExtensionType,
    MultilingualString,
    VersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/locationReferencing"


class AltitudeAccuracyEnum1(Enum):
    EQUAL_TO_OR_LESS_THAN1_CENTIMETRE = "equalToOrLessThan1Centimetre"
    EQUAL_TO_OR_LESS_THAN2_CENTIMETRES = "equalToOrLessThan2Centimetres"
    EQUAL_TO_OR_LESS_THAN5_CENTIMETRES = "equalToOrLessThan5Centimetres"
    EQUAL_TO_OR_LESS_THAN10_CENTIMETRES = "equalToOrLessThan10Centimetres"
    EQUAL_TO_OR_LESS_THAN20_CENTIMETRES = "equalToOrLessThan20Centimetres"
    EQUAL_TO_OR_LESS_THAN50_CENTIMETRES = "equalToOrLessThan50Centimetres"
    EQUAL_TO_OR_LESS_THAN1_METRE = "equalToOrLessThan1Metre"
    EQUAL_TO_OR_LESS_THAN2_METRES = "equalToOrLessThan2Metres"
    EQUAL_TO_OR_LESS_THAN5_METRES = "equalToOrLessThan5Metres"
    EQUAL_TO_OR_LESS_THAN10_METRES = "equalToOrLessThan10Metres"
    EQUAL_TO_OR_LESS_THAN20_METRES = "equalToOrLessThan20Metres"
    EQUAL_TO_OR_LESS_THAN50_METRES = "equalToOrLessThan50Metres"
    EQUAL_TO_OR_LESS_THAN100_METRES = "equalToOrLessThan100Metres"
    EQUAL_TO_OR_LESS_THAN200_METRES = "equalToOrLessThan200Metres"
    EXTENDED = "_extended"


class HeightTypeEnum1(Enum):
    ELLIPSOIDAL_HEIGHT = "ellipsoidalHeight"
    GRAVITY_RELATED_HEIGHT = "gravityRelatedHeight"
    RELATIVE_HEIGHT = "relativeHeight"
    EXTENDED = "_extended"


class OpenlrFormOfWayEnum1(Enum):
    UNDEFINED = "undefined"
    MOTORWAY = "motorway"
    MULTIPLE_CARRIAGEWAY = "multipleCarriageway"
    SINGLE_CARRIAGEWAY = "singleCarriageway"
    ROUNDABOUT = "roundabout"
    SLIP_ROAD = "slipRoad"
    TRAFFIC_SQUARE = "trafficSquare"
    OTHER = "other"
    EXTENDED = "_extended"


class OpenlrFunctionalRoadClassEnum1(Enum):
    FRC0 = "frc0"
    FRC1 = "frc1"
    FRC2 = "frc2"
    FRC3 = "frc3"
    FRC4 = "frc4"
    FRC5 = "frc5"
    FRC6 = "frc6"
    FRC7 = "frc7"
    EXTENDED = "_extended"


class OpenlrOrientationEnum1(Enum):
    NO_ORIENTATION_OR_UNKNOWN = "noOrientationOrUnknown"
    WITH_LINE_DIRECTION = "withLineDirection"
    AGAINST_LINE_DIRECTION = "againstLineDirection"
    BOTH = "both"
    EXTENDED = "_extended"


class OpenlrSideOfRoadEnum1(Enum):
    ON_ROAD_OR_UNKNOWN = "onRoadOrUnknown"
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"
    EXTENDED = "_extended"


class PositionConfidenceCodedErrorEnum1(Enum):
    OUT_OF_RANGE = "outOfRange"
    UNAVAILABLE = "unavailable"
    EXTENDED = "_extended"


@dataclass
class LocationReference:
    location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrOffsets:
    openlr_positive_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrPositiveOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    openlr_negative_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNegativeOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    openlr_offsets_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrOffsetsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrPointLocationReference:
    openlr_point_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPointLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class PositionAccuracy:
    accuracy_percentile50: Optional[float] = field(
        default=None,
        metadata={
            "name": "accuracyPercentile50",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    accuracy_percentile75: Optional[float] = field(
        default=None,
        metadata={
            "name": "accuracyPercentile75",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    accuracy_percentile95: Optional[float] = field(
        default=None,
        metadata={
            "name": "accuracyPercentile95",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    position_accuracy_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_positionAccuracyExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class RoadInformation:
    road_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        },
    )
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_length": 1024,
        },
    )
    road_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class AltitudeAccuracyEnum2:
    class Meta:
        name = "_AltitudeAccuracyEnum"

    value: Optional[AltitudeAccuracyEnum1] = field(
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
class HeightTypeEnum2:
    class Meta:
        name = "_HeightTypeEnum"

    value: Optional[HeightTypeEnum1] = field(
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
class OpenlrFormOfWayEnum2:
    class Meta:
        name = "_OpenlrFormOfWayEnum"

    value: Optional[OpenlrFormOfWayEnum1] = field(
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
class OpenlrFunctionalRoadClassEnum2:
    class Meta:
        name = "_OpenlrFunctionalRoadClassEnum"

    value: Optional[OpenlrFunctionalRoadClassEnum1] = field(
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
class OpenlrOrientationEnum2:
    class Meta:
        name = "_OpenlrOrientationEnum"

    value: Optional[OpenlrOrientationEnum1] = field(
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
class OpenlrSideOfRoadEnum2:
    class Meta:
        name = "_OpenlrSideOfRoadEnum"

    value: Optional[OpenlrSideOfRoadEnum1] = field(
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
class PositionConfidenceCodedErrorEnum2:
    class Meta:
        name = "_PositionConfidenceCodedErrorEnum"

    value: Optional[PositionConfidenceCodedErrorEnum1] = field(
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
class PredefinedLocationVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedLocationVersionedReference"

    target_class: str = field(
        init=False,
        default="loc:PredefinedLocation",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AltitudeConfidence:
    altitude_accuracy_coded_value: Optional[AltitudeAccuracyEnum2] = field(
        default=None,
        metadata={
            "name": "altitudeAccuracyCodedValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    altitude_accuracy_coded_error: Optional[
        PositionConfidenceCodedErrorEnum2
    ] = field(
        default=None,
        metadata={
            "name": "altitudeAccuracyCodedError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    altitude_confidence_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_altitudeConfidenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrLineAttributes:
    openlr_functional_road_class: Optional[OpenlrFunctionalRoadClassEnum2] = (
        field(
            default=None,
            metadata={
                "name": "openlrFunctionalRoadClass",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/locationReferencing",
                "required": True,
            },
        )
    )
    openlr_form_of_way: Optional[OpenlrFormOfWayEnum2] = field(
        default=None,
        metadata={
            "name": "openlrFormOfWay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 359,
        },
    )
    openlr_line_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrLineAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrPathAttributes:
    openlr_lowest_frc_to_next_lrpoint: Optional[
        OpenlrFunctionalRoadClassEnum2
    ] = field(
        default=None,
        metadata={
            "name": "openlrLowestFrcToNextLRPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_distance_to_next_lrpoint: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrDistanceToNextLRPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_path_attributes_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPathAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class PositionConfidenceEllipse:
    semi_major_axis_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    semi_major_axis_length_coded_error: Optional[
        PositionConfidenceCodedErrorEnum2
    ] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisLengthCodedError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    semi_minor_axis_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "semiMinorAxisLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    semi_minor_axis_length_coded_error: Optional[
        PositionConfidenceCodedErrorEnum2
    ] = field(
        default=None,
        metadata={
            "name": "semiMinorAxisLengthCodedError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    semi_major_axis_orientation: Optional[int] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisOrientation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_inclusive": 0,
            "max_inclusive": 359,
        },
    )
    semi_major_axis_orientation_error: Optional[bool] = field(
        default=None,
        metadata={
            "name": "semiMajorAxisOrientationError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    position_confidence_ellipse_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_positionConfidenceEllipseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class SupplementaryPositionalDescription:
    location_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "locationDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    road_information: List[RoadInformation] = field(
        default_factory=list,
        metadata={
            "name": "roadInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    supplementary_positional_description_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "_supplementaryPositionalDescriptionExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/locationReferencing",
            },
        )
    )


@dataclass
class HeightCoordinate:
    height_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "heightValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    height_type: Optional[HeightTypeEnum2] = field(
        default=None,
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    altitude_confidence: Optional[AltitudeConfidence] = field(
        default=None,
        metadata={
            "name": "altitudeConfidence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    vertical_position_accuracy: Optional[PositionAccuracy] = field(
        default=None,
        metadata={
            "name": "verticalPositionAccuracy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    height_coordinate_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_heightCoordinateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class PointCoordinates:
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    height_coordinate: List[HeightCoordinate] = field(
        default_factory=list,
        metadata={
            "name": "heightCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "max_occurs": 3,
        },
    )
    position_confidence_ellipse: Optional[PositionConfidenceEllipse] = field(
        default=None,
        metadata={
            "name": "positionConfidenceEllipse",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    horizontal_position_accuracy: Optional[PositionAccuracy] = field(
        default=None,
        metadata={
            "name": "horizontalPositionAccuracy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    point_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class Location(LocationReference):
    coordinates_for_display: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "coordinatesForDisplay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrBaseReferencePoint:
    openlr_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_line_attributes: Optional[OpenlrLineAttributes] = field(
        default=None,
        metadata={
            "name": "openlrLineAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_base_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrBaseReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrGeoCoordinate(OpenlrPointLocationReference):
    openlr_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_geo_coordinate_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrGeoCoordinateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class PointByCoordinates:
    bearing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "min_inclusive": 0,
            "max_inclusive": 359,
        },
    )
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    point_by_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointByCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class LocationByReference(Location):
    predefined_location_reference: Optional[
        PredefinedLocationVersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "predefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    location_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class NetworkLocation(Location):
    supplementary_positional_description: Optional[
        SupplementaryPositionalDescription
    ] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    network_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrLastLocationReferencePoint(OpenlrBaseReferencePoint):
    openlr_last_location_reference_point_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "_openlrLastLocationReferencePointExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/locationReferencing",
            },
        )
    )


@dataclass
class OpenlrLocationReferencePoint(OpenlrBaseReferencePoint):
    openlr_path_attributes: Optional[OpenlrPathAttributes] = field(
        default=None,
        metadata={
            "name": "openlrPathAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrBasePointLocation(OpenlrPointLocationReference):
    openlr_side_of_road: Optional[OpenlrSideOfRoadEnum2] = field(
        default=None,
        metadata={
            "name": "openlrSideOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_orientation: Optional[OpenlrOrientationEnum2] = field(
        default=None,
        metadata={
            "name": "openlrOrientation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_location_reference_point: Optional[OpenlrLocationReferencePoint] = (
        field(
            default=None,
            metadata={
                "name": "openlrLocationReferencePoint",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/locationReferencing",
                "required": True,
            },
        )
    )
    openlr_last_location_reference_point: Optional[
        OpenlrLastLocationReferencePoint
    ] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
            "required": True,
        },
    )
    openlr_offsets: Optional[OpenlrOffsets] = field(
        default=None,
        metadata={
            "name": "openlrOffsets",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    openlr_base_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrBasePointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class PointLocation(NetworkLocation):
    point_by_coordinates: Optional[PointByCoordinates] = field(
        default=None,
        metadata={
            "name": "pointByCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
    openlr_point_location_reference: Optional[OpenlrPointLocationReference] = (
        field(
            default=None,
            metadata={
                "name": "openlrPointLocationReference",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/locationReferencing",
            },
        )
    )
    point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )


@dataclass
class OpenlrPointAlongLine(OpenlrBasePointLocation):
    openlr_point_along_line_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_openlrPointAlongLineExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/locationReferencing",
        },
    )
