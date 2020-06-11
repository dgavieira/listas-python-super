altura = float(input("Insira sua altura"))
peso = float(input("insira seu peso"))

#calculo do imc
imc = peso/(altura**2)
#inicializacao de condicionais
muito_abaixo_do_peso = False
abaixo_do_peso_normal = False
peso_dentro_do_normal = False
acima_do_peso_normal = False
muito_acima_do_peso = False

#verificação de faixa de peso
if imc < 17:
  muito_abaixo_do_peso = True
elif 17 <= imc < 18.5:
  abaixo_do_peso_normal = True
elif 18.5 <= imc < 25:
  peso_dentro_do_normal = True
elif 25 <= imc < 30:
  acima_do_peso_normal = True
elif imc >= 30:
  muito_acima_do_peso = True

#impressão conforme o enunciado
print("Muito abaixo do peso \t : \t{}".format(muito_abaixo_do_peso))
print("Abaixo do peso normal \t : \t{}".format(abaixo_do_peso_normal))
print("Peso dentro do normal \t : \t{}".format(peso_dentro_do_normal))
print("Acima do peso normal \t : \t{}".format(acima_do_peso_normal))
print("Muito acima do peso \t : \t{}".format(muito_acima_do_peso))