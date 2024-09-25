using DatexII;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace DemoSoapServer.Data
{
    public class DataManager : IDataManager
    {
    
    public MessageContainer GetData()
    {
            MessageContainer messageContainer = null;
            messageContainer = new MessageContainer();
            messageContainer.profileName = "SituationPublication Profile";
            messageContainer.exchangeInformation = new ExchangeInformation();
            messageContainer.exchangeInformation.exchangeContext = new ExchangeContext();
            messageContainer.exchangeInformation.exchangeContext.supplierOrCisRequester = new Agent();
            messageContainer.exchangeInformation.dynamicInformation = new DynamicInformation();
            messageContainer.exchangeInformation.exchangeContext.supplierOrCisRequester.internationalIdentifier = new InternationalIdentifier();
            messageContainer.exchangeInformation.exchangeContext.supplierOrCisRequester.internationalIdentifier.nationalIdentifier = "DEMO";
            messageContainer.exchangeInformation.exchangeContext.supplierOrCisRequester.internationalIdentifier.country = "SE";
            messageContainer.exchangeInformation.dynamicInformation.messageGenerationTimestamp = DateTime.UtcNow;             
            
            // using (var httpClient = new HttpClient())
            // {
            //     //Get data from IRCA, The Icelandic Road and Coastal Administration
            //     //Open DATEX II 3.1 Service, using Soap and http get
            //     // This service includes point incidents using same exchange profile and payload profile as in this example
            //     using (var response = httpClient.GetAsync("http://datex.vegagerdin.is/situationpublication3_1/SituationService/pullsnapshotdata").Result)
            //     {
            //         string apiResponse = response.Content.ReadAsStringAsync().Result;

            //         XmlSerializer serializer = new XmlSerializer(typeof(MessageContainer));
            //         StringReader reader = new StringReader(apiResponse);
            //         data = (MessageContainer)serializer.Deserialize(reader);

            //     }
            // }

            return messageContainer;

    }

    }
}
