from dataclasses import dataclass

from datex_snapshot_pull.situation_service_xsd_name_datexii_3_common import (
    PayloadPublication,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/d2Payload"


@dataclass
class Payload(PayloadPublication):
    class Meta:
        name = "payload"
        namespace = "http://datex2.eu/schema/3/d2Payload"
