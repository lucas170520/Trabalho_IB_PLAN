hora = int(input("Digite um a hora:  "))
if 0<=hora<=11:
    print("Está no horário da manhã")
elif 12<=hora<=17:
    print("Está no horário da tarde")
elif 18<=hora<=23:
    print("Está no horário da noite")
else:
    print("Hora invalida")
