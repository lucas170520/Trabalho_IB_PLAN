na = input("Digite o nome do aluno: ")
diciplina = input("Qual a diciplina: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
m = (nota1 + nota2)/2
if 0 <= m <6:
    print(f"{na} está reprovado na diciplina: {diciplina}")
elif 6 <= m <= 10: 
    print(f"{na} está aprovado na diciplina: {diciplina}")
