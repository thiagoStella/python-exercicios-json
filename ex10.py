'''Crie uma lista com números de 1 a 10 e, em seguida, crie uma segunda lista 
contendo somente os números pares. Salve somente a lista dos números pares em 
um arquivo pickle. Depois, abra novamente o arquivo pickle que salvou e mostre na tela o seu conteúdo.'''

import pickle

numeros = [1,2,3,4,5,6,7,8,9,10]


pares= []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
with open('pares.pickle','wb') as arquivo:
    pickle.dump(pares, arquivo)

with open('pares.pickle', 'rb') as arquivo:
    pares_lidos = pickle.load(arquivo)
    print(pares_lidos)