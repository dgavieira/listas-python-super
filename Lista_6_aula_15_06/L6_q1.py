lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(lista[0:10])
print(lista[8:14])
pares = [x for x in lista if x % 2 == 0]
print(pares)
impares = [ x for x in lista if x % 2 != 0]
print(impares)
multiplos = [x for x in lista if x % 2 == 0 and x % 3 == 0 and x % 4 == 0]
print(multiplos)
print(lista[::-1])