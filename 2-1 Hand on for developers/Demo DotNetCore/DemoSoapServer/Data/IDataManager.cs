using DemoSoapServer.Models;

namespace DemoSoapServer.Data
{
    public interface IDataManager
    {
        public MessageContainer GetData();
    }
}