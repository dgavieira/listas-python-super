#fatiamento da string para cálculo do primeiro dígito verificador
cpf = "01650067224"
cpf_slice = cpf[0:9]
verificacao = [int(dv) for dv in cpf[9:]]
dv = [int(dv) for dv in cpf[9:]]
val = [int(val) for val in cpf_slice]

#verificação do primeiro dígito
pesos_pdv = list(range(2,11))
pesos_pdv.reverse()
zipped = list(zip(val,pesos_pdv))
lista_soma = [i*j for i,j in zipped]
soma_primeiro_digito = sum(lista_soma)
#cálculo do primeiro dígito verificador
resto = soma_primeiro_digito % 11
pdv = 11 - resto

#fatiamento a string para cálculo do segundo dígito verificador
cpf_slice_2 = cpf[0:10]
print(cpf_slice_2)
dv = [int(dv) for dv in cpf[-1]]
val = [int(val) for val in cpf_slice_2]

#verificação do segundo dígito
pesos_sdv = list(range(2,12))
pesos_sdv.reverse()
zipped = list(zip(val, pesos_sdv))
lista_soma = [i*j for i,j in zipped]
soma_segundo_digito = sum(lista_soma)
#cálculo do segundo dígito verificador
resto = soma_segundo_digito % 11
sdv = 11 - resto

#Comparação do cálculo com o real
if pdv == verificacao[0] and sdv == verificacao[1]:
    print("CPF VÁLIDO")
else:
    print("CPF INVÁLIDO")
