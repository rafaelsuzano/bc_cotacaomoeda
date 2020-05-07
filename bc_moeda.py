
from suds.client import Client

from datetime import date,timedelta
#print (client) ## shows the details of this service
wsdl="https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl"
data = date.today() - timedelta(days=1)
data=(data.strftime("%d/%m/%Y") )

moedas_ids = [1,10813,21619,21620,21621,21622,21623,21624,21625,21626,21627,21628,21629,21630,21631,21632,21633,21634,21635,21636]


class Moedas():
    
    print("Fonte de dados Banco Central do Brasil")
    def dispatch_dict(operator):
            return {
            1: lambda: "Dólar (venda)",
            10813: lambda: "Dólar (Compra)",
            21619: lambda: "Euro (venda)",
            21620: lambda:"Euro (compra)",
            21621: lambda: "Iene (venda)",
            21622: lambda: "Iene (compra)",
            21623: lambda: "Libra esterlina (venda)",
            21624: lambda: "Libra esterlina (compra)",
            21625: lambda: "Franco Suíço (venda)",
            21626: lambda: "Franco Suíço (compra)",
            21627: lambda: "Coroa Dinamarquesa (venda)",
            21628: lambda: "Coroa Dinamarquesa (compra)",
            21629: lambda: "Coroa Norueguesa (venda)",
            21630: lambda: "Coroa Norueguesa (compra)",
            21631: lambda: "Coroa Sueca (venda)",
            21632: lambda: "Coroa Sueca (compra)",
            21633: lambda: "Dólar Australiano (venda)",
            21634: lambda: "Dólar Australiano (compra)",
            21635: lambda: "Dólar Canadense (venda)",
            21636: lambda: "Dólar Canadense (compra)",

                        }.get(operator, lambda: None)()


    def Retorna(moeda,data):
  
        client = Client(wsdl)
        result = client.service.getValor(moeda,data)
                    
 
        return result,moeda,data   

   
    for id in moedas_ids:
    
        valor,moeda,dia = Retorna(id,data)
        print("Moeda:"+dispatch_dict(moeda) ,"R$ "+valor,"Data:"+dia )
 
