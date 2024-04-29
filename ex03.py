'''Crie um programa que escreva um arquivo chamado "alunos.txt" contendo informações de alunos (um aluno por linha, separado por vírgulas - nome, idade, nota)'''

alunos = [
    ("João", 18, 9.5),
    ("Maria", 19, 8.7),
    ("Pedro", 20, 7.2),
    ("Ana", 18, 9.0),
    ("Carlos", 19, 8.5)
]

with open('alunos.txt','w') as arquivo:
    for aluno in alunos:
        linha = ', '.join(map(str,aluno)) +'\n'
        arquivo.write(linha)
