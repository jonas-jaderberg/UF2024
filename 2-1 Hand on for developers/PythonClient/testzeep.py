import zeep

wsdl = 'http://datex.vegagerdin.is/situationpublication3_1/SituationService?wsdl'
client = zeep.Client(wsdl=wsdl)
result = client.service.pullSnapshotData()
print(result)
print(len(result.payload[0].situation))
payload = result.payload
input_dict = zeep.helpers.serialize_object(result.payload[0].situation)
print(len(input_dict))