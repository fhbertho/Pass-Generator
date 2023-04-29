import random
import string

def generate_password(service, size, email):
    """Função para gerar senha aleatória"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(size))
    return {'service': service, 'email': email, 'password': password}

def save_password(password):
    """Função para salvar senha em um arquivo de texto"""
    with open('senhas.txt', 'a') as f:
        f.write(f'Serviço: {password["service"]}\n')
        f.write(f'E-mail: {password["email"]}\n')
        f.write(f'Senha: {password["password"]}\n\n')

# Obter as informações do usuário

service = input("Qual o serviço para a senha? ")
size = int(input("Qual o tamanho da senha? "))
email = input("Qual o e-mail registrado para senha? ")

# Gerar a senha e salvar em um arquivo de texto

password = generate_password(service, size, email)
save_password(password)
print('Sua senha é: '+ password)

