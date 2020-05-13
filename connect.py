import pymysql.cursors

class conectar(object):
        global db;

        def __init__(self):
                host = "localhost"
                user = "root"
                database = "cotacao"
                password = "12345678"
                try:
                        self.db = pymysql.connect(host=host,
                                                                database=database,
                                                                user=user,
                                                                password=password,
                                                                autocommit=True)
                        
                             
                except  pymysql.Error as err:
                                print("Alguma coisa deu errado !!!")
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
         

    