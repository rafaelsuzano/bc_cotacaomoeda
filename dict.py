
import pymongo

def __init__(self):

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["cotacao"]
    mycol = mydb["bc_moedas"]

    mydict = {'Moeda': 'C', 'Valor': '1', 'Data': '30/06/2016', 'Operacao': 'V'}

    x = mycol.insert_one(mydict)

    print(x)


'''
dados ={}
def Dados (moeda,valor,data,op):
  
    d = {'Moeda':moeda, 'Valor':valor, 'Data':data, 'Operacao':op}
    d["Moeda"] = "C"
    print(d)

Dados("M","1","30/06/2016","V")
'''