valor_hora = 19.35
horas_trabalhadas = 40*4

salario_bruto = valor_hora*horas_trabalhadas

ir = 0.11*salario_bruto
inss = 0.08*salario_bruto
sind = 0.05*salario_bruto
total_desc = ir + inss + sind

salario_liquido = salario_bruto - total_desc

print("Salário Bruto: R${:.2f} \n Imposto de Renda: R$ {:.2f} \n INSS: R$ {:.2f} \n Sindicato: R$ {:.2f} \n Total de Descontos: R$ {:.2f} \n Salário Líquido: R$ {:.2f}".format(salario_bruto,ir,inss,sind,total_desc,salario_liquido))