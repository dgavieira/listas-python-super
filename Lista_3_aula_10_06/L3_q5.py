'''
5) Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês a mês,
sem usar a fórmula de juros compostos.

O usuário deve informar quanto será investido por mês e qual será a taxa de juros mensal
O programa deve informar o saldo do investimento após um ano (soma das aplicações mês a mês mais os juros),
e perguntar ao usuário se ele deseja que seja calculado o ano seguinte, sucessivamente
Por exemplo, caso o usuário deseje investir R$ 100,00 por mês, e tenha uma taxa de juros de 1% ao mês,
o programa forneceria a seguinte saída:

Saldo do investimento após 1 ano: R$ 1268.2

Deseja processar mais um ano? (S/N)
'''
flag = 's'
invest_inicial = 100.00
valor_mensal = 100.00
taxa = 1.00
taxa = taxa/100
rend_ano = 0
rend_mes = invest_inicial + taxa*invest_inicial
ano = 1
while flag.lower() == 's':
    for mes in range(12):
        rend_mes = valor_mensal*taxa + rend_mes
        rend_ano = rend_ano + rend_mes
    print("Saldo do investimento após {} ano(s): R${:.2f}".format(ano, rend_ano))
    flag = str(input("Deseja Processar mais um ano? (S/N)"))
    ano = ano + 1

else:
    print("Cálculo encerrado")
