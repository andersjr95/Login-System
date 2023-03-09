import os
import json
import getpass
# from hashlib import sha256

def bem_vindo():
    print("Registration / Login System")
    print("*" * 27)
    print("1. List\n2. Registration\n3. Login\n4. Delete Registration\n5. Exit\n")


def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        usuarios = []
        with open("usuarios.json", "x") as arquivo:
            json.dump(usuarios, arquivo)
        print("\nWe don't have registered users yet")
    return usuarios


def listar_usuarios():
    usuarios = carregar_usuarios()

    for i, usuario in enumerate(usuarios, start=1):
        print(f"User: {i} - {usuario['id']}")


def cadastrar():
    usuarios = carregar_usuarios()
    usuarios_existente = False
    senha_ok = False

    novo_usuario = {
        "id": input("\nRegister a User: ").lower(),
        "senha": getpass.getpass("\nRegister a password: ")
    }
    confirmar_senha = getpass.getpass("\nConfirm the password: ")

    if novo_usuario["id"] == "":
        print("\nUser blank, Required.")
    elif len(novo_usuario["id"]) <= 4:
        print("\nUsername too short.")
    elif novo_usuario["id"] and novo_usuario["id"][0].isdigit():
        print("\nUser MUST start with LETTER")
    else:
        for usuario in usuarios:
            if usuario["id"] == novo_usuario["id"]:
                usuarios_existente = True
                break

    if novo_usuario["senha"] != confirmar_senha:
        print("\nPasswords do not match.")
    elif novo_usuario["senha"] == "":
        print("\nPassword blank, required.")
    elif len(novo_usuario["senha"]) <= 4:
        print("\nPassword is too short.")
    else:
        senha_ok = True
        
        if usuarios_existente:
            print("\nUser already registered.")
        elif usuarios_existente == False and senha_ok == True:
            usuarios.append(novo_usuario)
            print("\nSuccessfully registered user!")
        
        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo)


def logar():
    usuarios = carregar_usuarios()

    logar_usuario = input("\nEnter your username: ").lower()
    logar_senha = getpass.getpass("Digite sua Senha: ")

    for usuario in usuarios:
        if logar_usuario == "" or logar_senha == "":
            print("\nUsername or Password blank, required.")
            break
        elif logar_usuario == usuario["id"] and logar_senha != usuario["senha"]:
            print("\nLogin failed.")
            break
        elif logar_usuario != usuario["id"] and logar_senha == usuario["senha"]:
            print("\nLogin failed.")
            break
        else:
            logar_usuario == usuario["id"] and logar_senha == usuario["senha"]
            print("\nLogin Successfully Done.")
            print(f"\nWelcome back '{logar_usuario}'.")
            break


def excluir():
    usuarios = carregar_usuarios()

    deletar_usuario = input("\nDigite o Usuário que deseja Deletar: ").lower()

    usuario_deletar = None

    for i, usuario in enumerate(usuarios):
        if usuario["id"] == deletar_usuario:
            usuario_deletar = i
            break

    if usuario_deletar is not None:
        senha = getpass.getpass("\nDigite sua Senha: ")
        confirmar_senha = getpass.getpass("Confirme sua Senha: ")

        if senha != confirmar_senha:
            print("\nAs Senhas não Conferem.")
        else:
            if usuario["senha"] == senha:
                del usuarios[usuario_deletar]
                print("\nUsuário deletado com Sucesso!")
            else:
                print("\nUsuário ou Senha não conferem.")
    else:
        print("\nUsuário não encontrado.")

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)


def finalizar():
    enter = input("\nType 'ENTER' to continue.")
    os.system("cls")


while True:
    bem_vindo()
    resposta = input("What action do you want to perform? [1], [2], [3], [4] or [5]\nResponse: ")

    if resposta == "1":
        listar_usuarios()
    elif resposta == "2":
        cadastrar()
    elif resposta == "3":
        logar()
    elif resposta == "4":
        excluir()
    elif resposta == "5":
        print("\nSee you soon!")
        break
    else:
        print("\nType only: 1, 2, 3, 4 or 5")

    
    finalizar()