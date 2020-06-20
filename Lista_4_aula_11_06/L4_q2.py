data_nasc = "29/10/1973"
chave = str(data_nasc[3:5])
dia = data_nasc[0:2]
mes = chave
ano = data_nasc[6::]

print(chave, dia, mes, ano)

dic_mes = {
    '01':'janeiro',
    '02':'feveriro',
    '03':'março',
    '04':'abril',
    '05':'maio',
    '06':'junho',
    '07':'julho',
    '08':'agosto',
    '09':'setembro',
    '10':'outubro',
    '11':'novembro',
    '12':'dezembro'
}

if chave in dic_mes:
    valor = dic_mes[chave]
    print(valor)
    print("Você nasceu em {} de {} de {}".format(dia,valor,ano))
else:
    print("data inválida")


