entrada = "AATCTGCAC"
lista_entrada = list(entrada)
lista_saida = []

dna = {
    'T':'A',
    'A':'T',
    'C':'G',
    'G':'C'
}

for i in lista_entrada:
    if i in dna:
        complementar = dna[i]
        lista_saida.append(complementar)

print(lista_entrada)
print(lista_saida)