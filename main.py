import os
import json
import getpass
# from hashlib import sha256

def bem_vindo():
    print("Sistema de Cadastro / Login")
    print("*" * 27)
    print("1. Listar\n2. Cadastro\n3. Login\n4. Excluir Cadastro\n5. Sair\n")


def listar_usuarios():
    usuarios = []

    if os.path.isfile("usuarios.json"):
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    else:
        print("\nAinda não temos usuários cadastrados.")

    for i, usuario in enumerate(usuarios):
        print("Usuário: ", i+1, "-", usuario["id"])


def cadastrar():
    usuarios = []
    usuarios_existente = False
    senha_ok = False

    if os.path.isfile("usuarios.json"):
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

    novo_usuario = {
        "id": input("\nCadastre um Usuário: ").lower(),
        "senha": getpass.getpass("\nCadastre uma Senha: ")
    }
    confirmar_senha = getpass.getpass("\nConfirme a Senha: ")

    if novo_usuario["id"] == "":
        print("\nUsuário em Branco, Obrigatório Preencher.")
    elif len(novo_usuario["id"]) <= 4:
        print("\nUsuário com nome muito curto.")
    elif novo_usuario["id"] and novo_usuario["id"][0].isdigit():
        print("\nUsuário DEVE começar com LETRA")
    else:
        for usuario in usuarios:
            if usuario["id"] == novo_usuario["id"]:
                usuarios_existente = True
                break

    if novo_usuario["senha"] != confirmar_senha:
        print("\nSenhas não conferem.")
    elif novo_usuario["senha"] == "":
        print("\nSenha em Branco, Obrigatório Preencher.")
    elif len(novo_usuario["senha"]) <= 4:
        print("\nSenha muito curta.")
    else:
        senha_ok = True
        
        if usuarios_existente:
            print("\nUsuário já cadastrado.")
        elif usuarios_existente == False and senha_ok == True:
            usuarios.append(novo_usuario)
            print("\nUsuário cadastrado com Sucesso!")
        
        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo)


def logar():
    usuarios = []

    if os.path.isfile("usuarios.json"):
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        logar_usuario = input("\nDigite seu Usuário: ").lower()
        logar_senha = getpass.getpass("Digite sua Senha: ")

        for usuario in usuarios:
            if logar_usuario == "" or logar_senha == "":
                print("\nUsuário ou Senha em Branco, Obrigatório Preencher.")
                break
            elif logar_usuario == usuario["id"] and logar_senha != usuario["senha"]:
                print("\nLogin NÃO Realizado.")
                break
            elif logar_usuario != usuario["id"] and logar_senha == usuario["senha"]:
                print("\nLogin NÃO Realizado.")
                break
            else:
                logar_usuario == usuario["id"] and logar_senha == usuario["senha"]
                print("\nLogin Realizado com Sucesso.")
                print(f"\nQue bom que voltou '{logar_usuario}'.")
                break


def excluir():
    usuarios = []

    if os.path.isfile("usuarios.json"):
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

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
    enter = input("\nDigite 'ENTER' para Continuar.")
    os.system("cls")


while True:
    bem_vindo()
    resposta = input("Qual ação deseja realizar? [1], [2], [3], [4] ou [5]\nResposta: ")

    if resposta == "1":
        listar_usuarios()
        finalizar()
    elif resposta == "2":
        cadastrar()
        finalizar()
    elif resposta == "3":
        logar()
        finalizar()
    elif resposta == "4":
        excluir()
        finalizar()
    elif resposta == "5":
        print("\nAté Breve!")
        break
    else:
        print("\nDigite apenas: 1, 2, 3, 4 ou 5")
        finalizar()