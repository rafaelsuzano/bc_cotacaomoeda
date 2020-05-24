import pymysql

#import pymysql.cursors
import json
class conectar(object):
        global db;
        
  
        def __init__(self):
                host = "localhost"
                user = "root"
                database = "cotacao"
                password = "12345678"
                port =3310
                try:
                        self.db = pymysql.connect(host=host,
                                                                database=database,
                                                                port=port,
                                                                user=user,
                                                                password=password,
                                                                autocommit=True)
                        
                             
                except  pymysql.Error as err:
                                print(err)
                                exit()
                else:
                        return 

               
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

