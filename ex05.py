# Crie um programa que leia o arquivo "alunos.txt" do exercício anterior. Em seguida, calcule a média das notas dos alunos e exiba na saída padrão

with open('alunos.txt','r') as arquivo:
    notas = []
    for linha in arquivo:
        dados = linha.split(',') # quebra a str em indices...
        notas.append(float(dados[2])) # ... e pega o terceiro indice

    media = sum(notas) / len(notas)
    print('A média das notas é: ', media)

