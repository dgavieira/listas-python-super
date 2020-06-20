linhas = int(input("insira número de linhas"))
colunas = int(input("insira número de colunas"))

ext = []
for i in range(colunas):
    inte = []
    for j in range(linhas):
        termo = input("insira o termpo")
        inte.append(termo)
    ext.append(inte)

print(ext)
