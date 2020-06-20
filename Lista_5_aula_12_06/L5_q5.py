def funcao(lista):
    print(lista)

lista = []
parametro = ''
while parametro != 'para':
    parametro = input("insira parâmetro. para para interromper")
    if parametro != 'para':
        lista.append(parametro)

funcao(lista)