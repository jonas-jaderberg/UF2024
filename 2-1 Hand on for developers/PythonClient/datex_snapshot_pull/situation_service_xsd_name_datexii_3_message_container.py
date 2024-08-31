from dataclasses import dataclass, field
from typing import List, Optional

from datex_snapshot_pull.situation_service_xsd_name_datexii_3_common import (
    ExtensionType,
    PayloadPublication,
)
from datex_snapshot_pull.situation_service_xsd_name_datexii_3_exchange_information import (
    ExchangeInformation as SituationServiceXsdNameDatexii3ExchangeInformationExchangeInformation,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/messageContainer"


@dataclass
class MessageContainer1:
    class Meta:
        name = "MessageContainer"

    payload: List[PayloadPublication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/messageContainer",
        },
    )
    exchange_information: Optional[
        SituationServiceXsdNameDatexii3ExchangeInformationExchangeInformation
    ] = field(
        default=None,
        metadata={
            "name": "exchangeInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/messageContainer",
            "required": True,
        },
    )
    message_container_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_messageContainerExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/messageContainer",
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
    extension_name: str = field(
        default="Exchange 2018",
        metadata={
            "name": "extensionName",
            "type": "Attribute",
        },
    )
    extension_version: str = field(
        default="1",
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
class ExchangeInformation(
    SituationServiceXsdNameDatexii3ExchangeInformationExchangeInformation
):
    class Meta:
        name = "exchangeInformation"
        namespace = "http://datex2.eu/schema/3/messageContainer"


@dataclass
class MessageContainer(MessageContainer1):
    class Meta:
        name = "messageContainer"
        namespace = "http://datex2.eu/schema/3/messageContainer"
