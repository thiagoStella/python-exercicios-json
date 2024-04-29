'''Crie um dicionário com o nome e a profissão de duas pessoas e adicione 
uma terceira pessoa com nome e profissão. Salve o resultado em um arquivo JSON'''
import json

funcionarios = {}
for i in range(2):
    nome = input('Digite o nome: ')
    profissao = input('Digite a profissão: ')
    funcionarios[nome] = profissao

nome = input('Digite o nome da terceira pessoa: ')
profissao = input('DIgite a profissão da terceira pessoa:')
funcionarios[nome] = profissao

with open('funcionarios.json', 'w') as arquivo:
    json.dump(funcionarios, arquivo)
