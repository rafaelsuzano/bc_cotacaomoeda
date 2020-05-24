select STR_TO_DATE(dt_cotacao, "%d/%m/%Y")as "Data",count(dt_cotacao) as "Total_Cotacao" from hist_cotacao group by dt_cotacao
order by STR_TO_DATE(dt_cotacao, "%d/%m/%Y") desc;



SELECT STR_TO_DATE(dt_cotacao, "%d/%m/%Y"),dt_cotacao from hist_cotacao



create table hist_cotacao 
(
id_hist_cotacao INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_moeda int,
valor decimal(10,7),
dt_cotacao varchar(10)
)



select  m.moeda_descr ,hc.valor , DATE_FORMAT(str_to_date(dt_cotacao, "%d/%m/%Y"), "%d/%m/%Y")as "DT_CTO", m.tipo from hist_cotacao hc 
inner join moedas m on m.id_moeda = hc.id_moeda

where 

STR_TO_DATE(dt_cotacao, "%d/%m/%Y") >= "1999/12/31"
order by   m.moeda_descr , hc.dt_cotacao ;



select * from moedas ;


---delete from hist_cotacao hc where dt_cotacao = "15/05/2020";