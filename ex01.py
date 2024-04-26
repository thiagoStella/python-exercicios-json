import json

lista_numeros = []
for i in range(5):
    numero = int(input('Digite um numero: '))
    lista_numeros.append(numero)

with open('números.txt', 'w') as arquivo:
    for numero in lista_numeros:
        arquivo.write(str(numero) + '\n')
print(lista_numeros)