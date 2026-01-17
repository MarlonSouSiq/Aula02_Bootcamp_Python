import math


#nome_aluno="gustavo@gmail.com"
#print(nome_aluno.split("@"))

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#t_celsius=float(input("Entre com a temperaturs em Celsius: "))
#t_Fahrenheit= (t_celsius * 1.8) + 32
#print(f" A temperatua  {t_celsius} graus celsius equivale a {t_Fahrenheit} graus Fahrenheit")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio=float(input("Entre com o raio do circulo: "))
#area= math.pi * ( raio**2)
#print(f" A área do circulo é : {area}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data=input("Entre com a data no formato: dd/mm/aaaa\n") cntlk e ctrlc
# partes= data.split('/')
# print(f" Dia: {partes[0]}")
# print(f" Mes: {partes[1]}")
# print(f" Mes: {partes[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# a = input("Entre com a primeira frase: \n")
# b = input("Entre com a segunda frase: \n")
# c=a+b
# #print(c)
# print(f'{a+b}')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

try:
    a=float(input("Entre com o primeiro numero: "))
    b=float(input("Entre com o rsegundo numero: "))
    print(a/b) 
except ZeroDivisionError:
    print("divisão por zero")
except KeyboardInterrupt:
    print("Acho que vc não quis teclar")





