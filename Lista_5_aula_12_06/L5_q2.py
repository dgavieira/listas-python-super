def verifica_range(num):
    intervalo = list(range(-100,100))
    if num in intervalo:
        print("número {} está no intervalo de -100 a 100".format(num))
    else:
        print("número {} não está no intervalo de -100 a 100".format(num))

num = int(input("numero \t"))
verifica_range(num)