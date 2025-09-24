from zeep import Client

def get_capital(pais,):

    client =Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')
    
    return client.service.CapitalCity(pais) 
    

print(get_capital('US'))