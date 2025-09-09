from connect import conectar
import json
t = conectar()
dados=(t.retorna())
#print(dados)


def moeda_dict(moeda):
   # D = {"Moeda":"Coroa Norueguesa", "Valor":"0.5820000", "Data":"13/05/2020", "Operacao":"V"}     
    #D = {"Moeda":(moeda) +",Valor:0.5820000," +"Data:13/05/2020,"+ "Operacao:V"}   
    #M=   {'ID:'+(moeda) +","+ "Moeda:"+ (moeda) +","+"Operacao:"+op}  
    M=  {"Moeda:"+(moeda)}
    print(M)


#for x in M:


 #   dictMoeda(x)

'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["cotacao"]
mycol = mydb["moedas"]
#print(mydb)
x =
 mycol.insert_one(D)
'''
