from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datex_snapshot_pull.situation_service_xsd_name_datexii_3_common import (
    DataValue,
    ExtensionType,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/roadTrafficData"


@dataclass
class DateTimeValue(DataValue):
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        },
    )
    date_time_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_dateTimeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        },
    )
