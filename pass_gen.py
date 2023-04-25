import hashlib
import getpass
import json

# Definir o nome do arquivo que irá armazenar as senhas
PASSWORD_FILE = 'passwords.json'

# Pedir ao usuário para criar uma senha mestra
master_password = getpass.getpass("Digite a senha mestra: ")

# Criar um hash da senha mestra usando a função de hash SHA256
master_hash = hashlib.sha256(master_password.encode()).hexdigest()

# Definir as funções para criptografar e descriptografar as senhas
def encrypt(password, key):
    cipher = []
    for i in range(len(password)):
        key_c = key[i % len(key)]
        cipher_c = chr((ord(password[i]) + ord(key_c)) % 256)
        cipher.append(cipher_c)
    return ''.join(cipher)

def decrypt(cipher, key):
    password = []
    for i in range(len(cipher)):
        key_c = key[i % len(key)]
        password_c = chr((ord(cipher[i]) - ord(key_c)) % 256)
        password.append(password_c)
    return ''.join(password)

# Definir as funções para adicionar e recuperar senhas
def add_password():
    website = input("Digite o nome do website: ")
    username = input("Digite o nome de usuário: ")
    password = getpass.getpass("Digite a senha: ")
    encrypted_password = encrypt(password, master_hash)
    with open(PASSWORD_FILE, 'r') as f:
        passwords = json.load(f)
    passwords[website] = {'username': username, 'password': encrypted_password}
    with open(PASSWORD_FILE, 'w') as f:
        json.dump(passwords, f)

def get_password():
    website = input("Digite o nome do website: ")
    with open(PASSWORD_FILE, 'r') as f:
        passwords = json.load(f)
    if website in passwords:
        username = passwords[website]['username']
        encrypted_password = passwords[website]['password']
        password = decrypt(encrypted_password, master_hash)
        print(f"Nome de usuário: {username}")
        print(f"Senha: {password}")
    else:
        print("Website não encontrado")

# Definir o loop principal do programa
while True:
    print("\n1 - Adicionar senha")
    print("2 - Recuperar senha")
    print("3 - Sair")
    choice = input("Escolha uma opção: ")
    if choice == '1':
        add_password()
    elif choice == '2':
        get_password()
    elif choice == '3':
        break
    else:
        print("Opção inválida")