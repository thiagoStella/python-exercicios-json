''' A partir do exercício 8 e após mostrar o resultado na tela, peça novamente 
para que o usuário digite uma nova frase. Adicione esta nova frase no mesmo arquivo de
texto sem apagar o conteúdo que já estava lá, e mostre o resultado na tela.'''

nova_frase = input('Digote uma nova frase: ')

with open('frase.txt','a') as arquivo:
    arquivo.write('\n' + nova_frase)

with open('frase.txt','r') as arquivo:
    exibir_frase = arquivo.read()
    print(exibir_frase)