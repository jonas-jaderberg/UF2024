#from xsdata.formats.dataclass.client import Client
from zeep import Client
from zeep.helpers import serialize_object
from datex_snapshot_pull import *
from xsdata.formats.dataclass.parsers.dict import DictDecoder
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig
# Initialize the client
client = Client('http://datex.vegagerdin.is/situationpublication3_1/SituationService?wsdl')

# Create an instance of the generated data class
#request = SnapshotPullInterfacePullSnapshotDataInput(body=SnapshotPullInterfacePullSnapshotDataInput())
#request = SnapshotPullInterfacePullSnapshotDataInput(body=SnapshotPullInterfacePullSnapshotDataInput())

# Call the SOAP service
response = client.service.pullSnapshotData()
print(response.modelBaseVersion)
# Serialize the response to a dictionary
response_dict = serialize_object(response.payload[0])

# Convert the dictionary to an xsData object#data_instance = MessageContainer1.from_dict(response_dict)

context = XmlContext()
config = ParserConfig()
decoder = DictDecoder(context=context,config=config)
data_instance = decoder.decode(response_dict, SituationPublication)

print(data_instance)
