d = {}
for i in range(0,2):
    mes = str(input("insira mês \n"))
    temperatura = float(input("insira temperatura \n"))
    d.update({mes:temperatura})

print(d.values())
print(d)
temp = list(d.values())
tam = len(temp)
soma = sum(temp)
med = soma/tam


print("temperatura média: {}ºC".format(med))