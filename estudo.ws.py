import xml.etree.ElementTree as ET
from zeep.exceptions import Fault
from zeep import Client

wsdl="https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl""

moedas = [[1,"Dolar (venda)"],[10813,"Dolar (Compra)"],[21619,"Euro (venda)"],[21620,"Euro (compra)"],[21621,"Iene (venda)"],[21622,"Iene (compra)"],[21623,"Libra esterlina (venda)"],[21624,"Libra esterlina (compra)"],[21625,"Franco Suíço (venda)"],[21626,"Franco Suíço (compra)"],[21627,"Coroa Dinamarquesa (venda)"],[21628,"Coroa Dinamarquesa (compra)"],[21629,"Coroa Norueguesa (venda)"],[21630,"Coroa Norueguesa (compra)"],[21631,"Coroa Sueca (venda)"],[21632,"Coroa Sueca (compra)"],[21633,"Dolar Australiano (venda)"],[21634,"Dolar Australiano (compra)"],[21635,"Dolar Canadense (venda)"],[21636,"Dolar Canadense (compra)"]]
cp

dia = '20/03/2022'


for m in moedas:
    try:    


        client = Client(wsdl)
        result = client.service.getValor(m[0],dia)
        
        print( m[1] +" - R$" + str(result['_value_1']))
    
    except:

        print("Sem cotação de " + (m[1]) + " para dia " + dia)


