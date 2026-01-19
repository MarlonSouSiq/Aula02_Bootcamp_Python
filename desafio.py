import os
import time


os.system("cls")

while True:
    nome=input("Entre com o seu nome: ")
    if nome == "":
        os.system("cls")
        print("Digite o seu nome")
    else:
        break

while True:
    try:
        salario=input("Entre com o seu salario: ")
        salario=float(salario.replace(",","."))
        break
    except ValueError:
        print("Digite um valor númerico")

while True:
    try:
        bonus=input("Entre com o seu Bonus: ")
        bonus=float(bonus.replace(",","."))
        break
    except ValueError:
        print("Digite um valor númerico")


adicional= 1000

os.system("cls")
salario_final= adicional+ salario*bonus
print(f"{nome}, O seu salario final será: {salario_final}")