import xml.etree.ElementTree as ET
from zeep.exceptions import Fault
from zeep import Client
import sys
from datetime import date,timedelta
import pandas as pd

wsdl="https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl"

moedas = [[1,"Dolar (venda)"],[10813,"Dolar (Compra)"],[21619,"Euro (venda)"],[21620,"Euro (compra)"],[21621,"Iene (venda)"],[21622,"Iene (compra)"],[21623,"Libra esterlina (venda)"],[21624,"Libra esterlina (compra)"],[21625,"Franco Suíço (venda)"],[21626,"Franco Suíço (compra)"],[21627,"Coroa Dinamarquesa (venda)"],[21628,"Coroa Dinamarquesa (compra)"],[21629,"Coroa Norueguesa (venda)"],[21630,"Coroa Norueguesa (compra)"],[21631,"Coroa Sueca (venda)"],[21632,"Coroa Sueca (compra)"],[21633,"Dolar Australiano (venda)"],[21634,"Dolar Australiano (compra)"],[21635,"Dolar Canadense (venda)"],[21636,"Dolar Canadense (compra)"]]
client = Client(wsdl)
datas =  []

df=pd.DataFrame({'Moeda':[],'Data':[],'Valor':[]})

    
for i in range(5):
    try:
        x= dataB = date.today() - timedelta(days=i)
        data=(x.strftime("%d/%m/%Y") )
    
        for m in moedas:
                
            result = client.service.getValor(m[0],data)
            df=df.append({"Moeda":m[1],"Data":data,"Valor":(result['_value_1'])},ignore_index=True)
           
    except:
            pass
            #opcional o print para exibir a mensagem de sem cotação
            print("Sem cotação  " + data )       



m= "Dolar (venda)"

def Filtro(m):
    print("Moeda: "+m)
    x=df.loc[(df['Moeda']== m)]
    selecionaColunas = x.iloc[:, [1,2]].to_string(index=False)

    print(selecionaColunas)

#Exibe todas as cotações
#print(df)

#Filtro por moeda

Filtro(m)
