n = int(input("Insira um número"))

while n <= 0:
  print("Número inválido")
else:
  print("Cálculo do fatorial")
  i = 1
  fat = 1
  while i <= n:
        fat = fat * i
        i = i + 1
print(fat)