idade = 0
altura = 1
cont = 0
while altura != 0:
  idade = int(input("Insira a idade"))
  altura = float(input("Insira a altura"))
  if idade > 18 and altura < 1.6:
    cont = cont + 1
else:
  print("Parada")
print("Existem {} alunos maiores que 18 anos com altura inferior a 1.6".format(cont))