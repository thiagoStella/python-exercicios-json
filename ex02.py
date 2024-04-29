#ler o arquivo "números" e mostrar a soma dos elementos
import json

soma = 0
with open('números.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        soma += int(linha)
    
print(soma)