SELECT id_moeda, moeda, operacao
FROM cotacao.moedas;

insert into moedas (id_moeda, moeda, operacao) 
values
(1, 'Dolar', 'V'),
(2, 'Dolar', 'C'),
(3, 'Euro', 'V'),
(4, 'Euro', 'C'),
(5, 'Iene', 'V'),
(6, 'Iene', 'C'),
(7, 'Libra esterlina', 'V'),
(8, 'Libra esterlina', 'C'),
(9, 'Franco Suíço', 'V'),
(10, 'Franco Suíço', 'C'),
(11, 'Coroa Dinamarquesa', 'V'),
(12, 'Coroa Dinamarquesa', 'C'),
(13, 'Coroa Norueguesa', 'V'),
(14, 'Coroa Norueguesa', 'C'),
(15, 'Coroa Sueca', 'V'),
(16, 'Coroa Sueca', 'C'),
(17, 'Dolar Australiano', 'V'),
(18, 'Dolar Australiano', 'C'),
(19, 'Dolar Canadense', 'V'),
(20, 'Dolar Canadense', 'C');


INSERT INTO moedas (id_moeda, moeda) VALUES
(100, 'BTC'),
(200, 'ETH'),
(300, 'BCH'),
(400, 'XRP'),
(700, 'USDC'),
(800, 'LTC'),
(900, 'CHZ');