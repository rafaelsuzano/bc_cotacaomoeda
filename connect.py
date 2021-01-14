#import pymysql
import mysql.connector



import json
class conectar(object):
        global db;
        
  
        def __init__(self):
                host = "prd-cotacao.mysql.uhserver.com"
                user = "root"
                database = "rsc1985"
                password = "Suz@no3001"
                port =3306
                try:
                        self.db = mysql.connector.connect(host=host,
                                                                database=database,
                                                                port=port,
                                                                user=user,
                                                                password=password,
                                                                autocommit=True,connect_timeout=1000)
                      
                           
                except mysql.connector.Error as err:
                    print("Deu ruim !!{}".format(err))
                    exit()        
               
        def inserir(self,id,dt,vlr):
                self.id = id
                self.data = dt
                self.tipo = vlr                
                
               
                cur = self.db.cursor()
                
                sql = ("insert into hist_cotacao (id_moeda,dt_cotacao,valor) values  (%s,%s,%s)")
                val = (id,dt,vlr)                   
                cur.execute(sql,val)
        
   
                
        def retorna(self):
                
                cur = self.db.cursor()
                cur.execute("SELECT * FROM moedas")

                resultado = cur.fetchall()

                return resultado
