'''Crie um código que peça para o usuário digitar uma frase. 
Salve o resultado em um arquivo de texto. Depois, abra este arquivo de
texto que salvou e mostre o resultado na tela'''

frase = input('Digite algo para ser salvo em um documento: ')

with open('frase.txt','w') as arquivo:
    arquivo.write(frase)

with open('frase.txt','r') as arquivo:
    exibir_frase = arquivo.read()
    print(exibir_frase)