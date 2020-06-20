perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Tinha dívivas com a vítima?",
             "Já trabalhou com a vítima?"]

pontos = 0
print("Responda sim ou não: \n")
for i in perguntas:
    print(i)
    res = str(input(""))
    if res.lower() == 'sim' or res.lower() == 's':
        pontos = pontos + 1
    elif res.lower() == 'nao' or res.lower() == 'não' or res.lower() == 'n':
        print("nada")

if pontos == 0:
    print("Inocente")
elif pontos == 1:
    print("Inocente")
elif pontos == 2:
    print("Suspeita")
elif pontos >= 3 and pontos <= 4:
    print("Cúmplice")
elif pontos == 5:
    print("Assassino")