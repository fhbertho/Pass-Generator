import random
import string

# Definir uma função para gerar uma senha forte
def generate_password(length=12):
    # Define os caracteres que podem ser usados na senha
    chars = string.ascii_letters + string.digits + string.punctuation

    # Gera uma senha aleatória usando os caracteres definidos
    password = ''.join(random.choice(chars) for _ in range(length))

    return password

# Pedir ao usuário quantas senhas eles desejam gerar
num_passwords = int(input("Quantas senhas deseja gerar? "))

# Pedir ao usuário o tamanho das senhas que eles desejam gerar
password_length = int(input("Qual o tamanho das senhas que deseja gerar? "))

# Gerar as senhas e armazená-las em um arquivo de texto
with open("/home/kali/Desktop/cyber_projects/senhas.txt", "a") as f:
    for i in range(num_passwords):
        service_name = input(f"Para qual serviço deseja gerar a senha {i+1}? ")
        password = generate_password(password_length)
        f.write(f"{service_name}: {password}\n")
        print(f"Senha {i+1} para {service_name}: {password}")