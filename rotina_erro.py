# try:
#     resultado=len(3)
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("Tudo bem")
    
# finally:
#     print("O importante é participar")

numero=input("Insira um número: ")
if isinstance(numero,int):
        print("O numero é um inteiro")
else:
        print("A variavel não é um inteiro")