entrada = "Hello World"
minusculas = entrada.lower()

conta_vogais = {}

for vogais in "aeiou":
    conta = minusculas.count(vogais)
    conta_vogais[vogais] = conta

print(conta_vogais)