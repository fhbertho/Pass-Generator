import random
import json

def gerar_senha(comprimento):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+={}[]'
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha
def adicionar_senha(servico, senha):
    with open('senhas.json', 'r') as arquivo:
        senhas = json.load(arquivo)
    senhas[servico] = senha
    with open('senhas.json', 'w') as arquivo:
        json.dump(senhas, arquivo, indent=4)

def recuperar_senha(servico):
    with open('senhas.json', 'r') as arquivo:
        senhas = json.load(arquivo)
    if servico in senhas:
        return senhas[servico]
    else:
        return None
while True:
    opcao = input("O que você deseja fazer? (G)erar nova senha, (A)dicionar senha existente ou (S)air: ")
    if opcao.lower() == 'g':
        servico = input("Qual é o serviço? ")
        comprimento = int(input("Qual é o comprimento da senha? "))
        senha = gerar_senha(comprimento)
        adicionar_senha(servico, senha)
        print("Senha gerada com sucesso!")
        print(f"A senha para {servico} é: {senha}")
    elif opcao.lower() == 'a':
        servico = input("Qual é o serviço? ")
        senha = input("Qual é a senha? ")
        adicionar_senha(servico, senha)
        print("Senha adicionada com sucesso!")
    elif opcao.lower() == 's':
        break
    else:
        print("Opção inválida. Tente novamente.")