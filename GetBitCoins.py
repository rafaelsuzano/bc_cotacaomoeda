# -*- coding: utf-8 -*-

import time
import os
from datetime import datetime,timedelta
import json
import requests
import string
import sys
import requests
from datetime import date
from connect import conectar
import pymysql
import datetime
from datetime import date,timedelta


class GetDataBitCoins():
        
            
        data = date.today() - timedelta(days=1)
        data=(data.strftime("%d/%m/%Y") )

        
        '''    
        ano =  data.year
        mes =  data.month 
        dia = data.day
            '''
        data = data.split("/")
        dia= (data[0])
        mes =(data[1])
        ano =(data[2])
            


     
        def CallBitCoins(Coin,ano,mes,dia):
            if Coin == "BTC" :
                id_moeda = 100
                coins = "BTC"
                
            elif Coin =="ETH" :
                 id_moeda = 200
                 coins = "ETH"

            elif Coin =="BCH":
                id_moeda = 300
                coins = "BCH"

            
            elif Coin =="XRP":
                 id_moeda = 400
                 coins = "XRP"

                    
            elif Coin =="USDC":
                id_moeda = 700
                coins = "USDC" 
           
            elif Coin == "LTC":
                id_moeda = 800
                coins = "LTC"
               
         
                      
            else:
                
                print("CriptoMoeda não cadastrada !!!")    
                return 999999
                sys.exit
            try:    
                url = 'https://www.mercadobitcoin.net/api/'+coins+'/day-summary/'+ ano+'/'+mes+'/'+dia +'/'
                r = requests.get(url)
                dados=(r.content)
                data = (json.loads(dados))
                data_c = data['date']
                closing = str(data['closing'])
                lowest = str(data['lowest'])
                opening = str(data['opening'])
                highest = str(data['highest'])
                volume = str(data['volume'])
                quantity = str(data['quantity'])
                amount = str(data['amount'])
                avg_price = str(data['avg_price'])

                
                t = conectar()     
                t.inserirCripto(data_c,closing,lowest,opening,highest,volume,quantity,amount,avg_price,id_moeda) 
                print(data_c,closing,lowest,opening,highest,volume,quantity,amount,avg_price,id_moeda)
                        
                return url
            except KeyError as error:
                print("Moeda:"+coins)
                print(data)
                print(error)
     
        CallBitCoins("USDC",(ano),(mes),(dia))
        CallBitCoins("BTC",(ano),(mes),(dia))
        CallBitCoins("ETH",(ano),(mes),(dia))
