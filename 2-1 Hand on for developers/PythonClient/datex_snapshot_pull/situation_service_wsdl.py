from dataclasses import dataclass, field
from typing import Optional

from datex_snapshot_pull.situation_service_xsd_name_datexii_3_message_container import (
    MessageContainer1,
)

__NAMESPACE__ = "http://datex2.eu/wsdl/snapshotPull/2020"


@dataclass
class SnapshotPullInterfacePullSnapshotDataInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[object] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )


@dataclass
class PullSnapshotDataOutput(MessageContainer1):
    class Meta:
        name = "pullSnapshotDataOutput"
        namespace = "http://datex2.eu/wsdl/snapshotPull/2020"


@dataclass
class SnapshotPullInterfacePullSnapshotDataOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["SnapshotPullInterfacePullSnapshotDataOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        pull_snapshot_data_output: Optional[PullSnapshotDataOutput] = field(
            default=None,
            metadata={
                "name": "pullSnapshotDataOutput",
                "type": "Element",
                "namespace": "http://datex2.eu/wsdl/snapshotPull/2020",
            },
        )
        fault: Optional[
            "SnapshotPullInterfacePullSnapshotDataOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


class SnapshotPullInterfacePullSnapshotData:
    style = "document"
    location = (
        "https://datex.vegagerdin.is/situationpublication3_1/SituationService"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://datex2.eu/wsdl/snapshotPull/2020/pullData"
    input = SnapshotPullInterfacePullSnapshotDataInput
    output = SnapshotPullInterfacePullSnapshotDataOutput
