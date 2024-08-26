from Classes.conta import Conta
import random

contas = []

while True:
    print("[1] - Cadastrar")
    print("[2] - Depositar")
    print("[3] - Sacar")
    print("[4] - Listar Dados")
    print("[0] - Sair")

    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            numConta = random.randint(0, 9999)
            titular = str(input("Digite seu nome: "))
            saldo = 0
            conta = Conta(numConta, titular, saldo)
            conta.cadastrar()
            contas.append(conta)
            print("Conta criada com sucesso!")
            print(f"O número da sua conta é: {numConta}")

        case 2:
            numConta = int(input("Digite o número da sua conta: "))
            valor = float(input("Digite o valor a ser depositado: "))
            for dadosContas in contas:
                if numConta == dadosContas.numConta:
                    deposito = dadosContas.depositar(valor)
                    print(f"R$ {valor:.2f} depositados com sucesso!")

        case 3:
            numConta = int(input("Digite o número da sua conta: "))
            valor = float(input("Digite o valor a ser sacado: "))
            for dadosContas in contas:
                if numConta == dadosContas.numConta:
                    saque = dadosContas.sacar(valor)
                    print(f"R$ {valor:.2f} sacados com sucesso!")

        case 4:
            numConta = int(input("Digite o número da sua conta: "))
            for dadosContas in contas:
                if numConta == dadosContas.numConta:
                    dadosConta = dadosContas.listarDados()
                    print(dadosConta)

        case 0:
            break