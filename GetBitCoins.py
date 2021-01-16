
projetos
MB_Cotacao_Moeda 
connect.py
import pymysql

import pymysql.cursors
import json
class conectar(object):
        global db;
        
  
        def __init__(self):
                host = "localhost"
                user = "root"
                database = "cotacao"
                password = "12345678"
                port = None
                #port =3310
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
        
   

        def inserirCripto(self,	data_c,closing,lowest,opening, highest,volume, quantity,amount, avg_price,id_moeda):
                
                self.data_c = data_c
                self.closing =closing
                self.lowest = lowest	
                self.opening = opening 
                self.highest = highest
                self.volume = volume 
                self.quantity =quantity
                self.amount =amount 
                self.avg_price = avg_price
                
                self.id_moeda = id_moeda
                
                data_c = "'" + data_c + "'"
                cur = self.db.cursor()

                  
                sql = """insert into hist_cotacao_cripto(data_c,closing,lowest,opening,highest,volume,quantity,amount,avg_price,id_moeda) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""%
                #print(sql)
                #print(val)
                cur.execute(sql,val)


        def UltimaCotacaDtaBitcoin(self):
                sql ="select  DATE_ADD((max(DATE_FORMAT(data_c,'%Y/%m/%d'))),interval 1 day) from  hist_cotacao_cripto_btc ;"
                cur = self.db.cursor()
                cur.execute(sql)  
                resultado = cur.fetchall()
                return resultado[0]


        def retorna(self):
             

                cur = self.db.cursor()
                cur.execute("SELECT * FROM moedas")
                resultado = cur.fetchone()
                return resultado

