# 21: Conversor de Temperatura
import os
import time

# def virgulaponto(numero_original):
#     numero_retorno = numero_original.replace(",",".")
#     return float(numero_retorno)
 

# while True: 
#     try:
#         os.system("cls")
#         t_celsius=input("Entre com a temperatura em Celsius: ")
#         t_celsiusok=virgulaponto(t_celsius)
#         t_Fahrenheit= (t_celsiusok * 1.8) + 32
#         print(f" A temperatura  {t_celsiusok} graus celsius equivale a {t_Fahrenheit} graus Fahrenheit")
#         break
#     except ValueError:
#         print("Valor digitado não é um número. Digite somente números")
#         time.sleep(2)
#         os.system("cls")

#22: Verificador de Palíndromo


#################################################################################
# os.system("cls")
# texto= input("Entre com o texto: ")
# letras_texto=list(texto)
# tamanho_texto=len(texto)
# print(letras_texto)

# for i in range (tamanho_texto):
    
#     if letras_texto[i] == letras_texto[tamanho_texto-1]:
#         palindromo=True
#     else:
#         palindromo= False
#         break
        
#     tamanho_texto -=1

# if palindromo:
#     print("Texto é um palindromo")
# else:    
#     print("Texto não é um palindromo")


############### Outra versão para palindromo
# def eh_palindromo(texto):
#     texto = texto.lower().replace(" ", "")
#     invertida = ""

#     for letra in texto:
#         invertida = letra + invertida

#     return texto == invertida

# texto = input("Digite um texto: ")

# if eh_palindromo(texto):
#     print("Texto é um palíndromo")
# else:
#     print("Texto não é um palíndromo")


# 23: Calculadora Simples

# os.system("cls")
# texto=input("Entre com a operação, sendo * para multiplicação, / para divisão: ")
# texto_sem_espaço= texto.replace(" ","")
# operadores = ["+", "-", "*", "/", "%", "="]
# numeros=["0", "1", "2", "3", "4", "5","6", "7", "8", "9"]
# letras_texto=list(texto_sem_espaço)
# tamanho_texto=len(texto_sem_espaço)

# for i in range (tamanho_texto):
#     if texto_sem_espaço[i] in operadores:
#         pos_operador=i
#         break
# operador=letras_texto[i]
# contador=0   
# primeiro_numero=""
# while contador<pos_operador:
#         primeiro_numero=primeiro_numero + texto_sem_espaço[contador]
#         contador += 1
    
# segundo_numero=""
# contador += 1
# while contador<tamanho_texto:
#         segundo_numero=segundo_numero + texto_sem_espaço[contador]
#         contador += 1

# expressao= primeiro_numero + operador + segundo_numero
# resultado= eval(expressao)
# print(f"Resultado : {resultado} ")


#calculadora 2

# os.system("cls")
# try:
#     texto=input("Entre com a operação, sendo * para multiplicação, / para divisão: ")
#     texto_sem_espaço= texto.replace(" ","")
#     resultado=eval(texto_sem_espaço)
#     print(f"O resultado é: {resultado}")  
# except NameError:
#     print("Valores digitados não são números. Digite somente números")

# except ZeroDivisionError: 
#     print("Divisão por zero")

    
# 24: Classificador de Números
# try:
#     os.system("cls")
#     while True:
#         numero=int(input("Digite um número: "))

#         if numero>0:
#             print("Numero positivo")
#         elif numero<0:
#             print("Numero Negativo")
#         else:
#             print("Zero")
#         if numero%2 == 0:
#             print("Numero Par")
#         else:
#             print("Numero impar")
# except ValueError:
#     print(" digite um número válido")




# 25: Conversão de Tipo com Validação

