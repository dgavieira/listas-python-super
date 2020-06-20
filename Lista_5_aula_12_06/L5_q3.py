def converte_horas(hora, minutos):
    if hora > 12:
        hora = hora - 12
        turno = "PM"
        print("{}:{} {}".format(hora, minutos, turno))
    else:
        turno = "AM"
        print("{}:{} {}".format(hora, minutos, turno))

hora = int(input("insira as horas"))
minutos = int(input("insira os minutos"))
converte_horas(hora, minutos)