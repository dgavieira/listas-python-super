#temp = 39
temp = float(input("Insira a temperatura"))
if temp < 37:
  print("Sem Febre")
elif temp >= 37 and temp < 39:
  print("Febril")
else:
  print("Febre Alta")