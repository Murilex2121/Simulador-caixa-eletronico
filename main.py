import os

saldo = 0.0
historico = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("=== Caixa Eletrônico ===")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Ver extrato")
    print("5. Sair")

def ver_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")

def depositar():
    global saldo
    valor = float(input("Digite o valor para depositar: R$ "))
    if valor > 0:
        saldo += valor
        historico.append(f"Depósito: +R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")

def sacar():
    global saldo
    valor = float(input("Digite o valor para sacar: R$ "))
    if 0 < valor <= saldo:
        saldo -= valor
        historico.append(f"Saque: -R$ {valor:.2f}")
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente ou valor inválido!")

def ver_extrato():
    print("=== Extrato ===")
    if not historico:
        print("Nenhuma movimentação.")
    else:
        for item in historico:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")

while True:
    limpar_tela()
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ver_saldo()
    elif opcao == "2":
        depositar()
    elif opcao == "3":
        sacar()
    elif opcao == "4":
        ver_extrato()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

    input("\nPressione Enter para continuar...")