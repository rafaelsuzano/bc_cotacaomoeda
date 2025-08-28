# -*- coding: utf-8 -*-
#import pymysql
import mysql.connector
import json
class conectar(object):
        global db;

                
  
        def __init__(self):
                host = "localhost"
                user = "root"
                database = "cotacao"
                password = "12345678"
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
                dt = "'"+ dt +"'"
                cur = self.db.cursor()
                sql = """insert into hist_cotacao_bc (id_moeda,dt_cotacao,valor) values  (%s,%s,%s)""" % (id,dt,vlr)
                cur.execute(sql)
               
        def retorna(self):
                
                cur = self.db.cursor()
                cur.execute("SELECT * FROM moedas")
                resultado = cur.fetchall()
                return resultado
        
        
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
               # closing = "'" + closing + "'"
                cur = self.db.cursor()                  
                sql = """insert into hist_cotacao_cripto(data_c,closing,lowest,opening,highest,volume,quantity,amount,avg_price,id_moeda) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""%(data_c,closing,lowest,opening,highest,volume,quantity,amount,avg_price,id_moeda)
                #print(sql)
                cur.execute(sql)
