from suds.client import Client
url = 'http://datex.vegagerdin.is/situationpublication3_1/SituationService?wsdl'
client = Client(url)
print(client)
result = client.service.pullSnapshotData()
print(result)
paylaod = result.payload

