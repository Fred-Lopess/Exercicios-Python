from Classes.funcionario import Funcionario
from Classes.cliente import Cliente
import random

dadosLoginFuncionarios = {}
dadosLoginClientes = {}

while True:
    print("[1] - Funcionário")
    print("[2] - Cliente")
    print("[0] - Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1 or escolha == 2 or escolha == 0:
        match escolha:
            case 1:
                print("[1] - Cadastrar")
                print("[2] - Entrar")
                print("[0] - Sair")
                escolha = int(input("Escolha uma opção: "))

                match escolha:
                    case 1:
                        nome = str(input("Digite seu nome: "))
                        email = str(input("Digite seu email: "))
                        cpf = int(input("Digite seu CPF: "))
                        senha = str(input("Digite sua senha: "))
                        idFuncionario = random.randint(0, 999)
                        funcionario = Funcionario(nome, email, cpf, senha, idFuncionario)
                        funcionario.cadastrar()
                        dadosLoginFuncionarios[cpf] = senha
                        print(f"Seja bem vindo(a) {nome}")

                    case 2:
                        cpf = int(input("Digite seu CPF: "))
                        senha = str(input("Digite sua senha: "))

                        if cpf in dadosLoginFuncionarios and dadosLoginFuncionarios[cpf] == senha:
                            print("Login efetuado com sucesso!")
                        else:
                            print("Informações inválidas!")

                    case 0:
                        break

            case 2:
                print("[1] - Cadastrar")
                print("[2] - Entrar")
                print("[0] - Sair")
                escolha = int(input("Escolha uma opção: "))

                match escolha:
                    case 1:
                        nome = str(input("Digite seu nome: "))
                        email = str(input("Digite seu email: "))
                        cpf = int(input("Digite seu CPF: "))
                        senha = str(input("Digite sua senha: "))
                        cliente = Cliente(nome, email, cpf, senha)
                        cliente.cadastrar()
                        dadosLoginClientes[cpf] = senha
                        print(f"Seja bem vindo(a) {nome}")

                    case 2:
                        cpf = int(input("Digite seu CPF: "))
                        senha = str(input("Digite sua senha: "))

                        if cpf in dadosLoginClientes and dadosLoginClientes[cpf] == senha:
                            print("Login efetuado com sucesso!")
                        else:
                            print("Informações inválidas!")

                    case 0:
                        break

            case 0:
                break
    else:
        print("Opção inválida!")