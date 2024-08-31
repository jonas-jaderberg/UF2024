from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datex_snapshot_pull.situation_service_xsd_name_datexii_3_common import (
    ExtensionType,
    InternationalIdentifier,
    MultilingualString,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/exchangeInformation"


class ExchangeReturnEnum1(Enum):
    FAIL = "fail"
    EXTENDED = "_extended"


class ExchangeStatusEnum1(Enum):
    UNDEFINED = "undefined"
    EXTENDED = "_extended"


class MessageTypeEnum1(Enum):
    PAYLOAD_DELIVERY = "payloadDelivery"
    OPEN_SESSION = "openSession"
    KEEP_ALIVE = "keepAlive"
    CLOSE_SESSION = "closeSession"
    RETURN = "return"
    CISSERVICE_REQUEST = "CISServiceRequest"
    CISFEEDBACK = "CISFeedback"
    EXTENDED = "_extended"


class ProtocolTypeEnum1(Enum):
    SNAPSHOT_PULL = "snapshotPull"
    EXTENDED = "_extended"


@dataclass
class Agent:
    international_identifier: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "internationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )
    agent_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_agentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )


@dataclass
class ExchangeReturnEnum2:
    class Meta:
        name = "_ExchangeReturnEnum"

    value: Optional[ExchangeReturnEnum1] = field(
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
class ExchangeStatusEnum2:
    class Meta:
        name = "_ExchangeStatusEnum"

    value: Optional[ExchangeStatusEnum1] = field(
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
class MessageTypeEnum2:
    class Meta:
        name = "_MessageTypeEnum"

    value: Optional[MessageTypeEnum1] = field(
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
class ProtocolTypeEnum2:
    class Meta:
        name = "_ProtocolTypeEnum"

    value: Optional[ProtocolTypeEnum1] = field(
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
class ExchangeContext:
    coded_exchange_protocol: Optional[ProtocolTypeEnum2] = field(
        default=None,
        metadata={
            "name": "codedExchangeProtocol",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
        },
    )
    exchange_specification_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "exchangeSpecificationVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
            "max_length": 1024,
        },
    )
    supplier_or_cis_requester: Optional[Agent] = field(
        default=None,
        metadata={
            "name": "supplierOrCisRequester",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
        },
    )
    exchange_context_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_exchangeContextExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )


@dataclass
class ReturnInformation:
    return_status: Optional[ExchangeReturnEnum2] = field(
        default=None,
        metadata={
            "name": "returnStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
        },
    )
    return_status_reason: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "returnStatusReason",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )
    return_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_returnInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )


@dataclass
class DynamicInformation:
    exchange_status: Optional[ExchangeStatusEnum2] = field(
        default=None,
        metadata={
            "name": "exchangeStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
        },
    )
    message_generation_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "messageGenerationTimestamp",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
        },
    )
    return_information: Optional[ReturnInformation] = field(
        default=None,
        metadata={
            "name": "returnInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )
    dynamic_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_dynamicInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )


@dataclass
class ExchangeInformation:
    message_type: Optional[MessageTypeEnum2] = field(
        default=None,
        metadata={
            "name": "messageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
        },
    )
    exchange_context: Optional[ExchangeContext] = field(
        default=None,
        metadata={
            "name": "exchangeContext",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
        },
    )
    dynamic_information: Optional[DynamicInformation] = field(
        default=None,
        metadata={
            "name": "dynamicInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
            "required": True,
        },
    )
    exchange_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_exchangeInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/exchangeInformation",
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
