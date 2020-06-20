entrada = "diego digo giovanni giovanni de alcantara alcantara vieira vieira vieira"
frase = list(entrada)
frase = frase.lower().replace('.','').replace(',','').replace('\n',' ').split(" ")
frase.sort()
frase_copia = frase.copy()

for i in frase_copia:
    while frase_copia(i) > 1:
        frase_copia.remove(i)

for i in frase_copia:
    print("A palavra {} ocorreu {} vezes".format(i, frase.count(i)))
