# Criando um Sistema Bancário

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    →"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f} \n"
            print("Depósito realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado não é válido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Valor excedeu limite de saque permitido.")
        
        elif excedeu_saques:
            print("Operação falhou! Número de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f} \n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        
        else:
            print("Operação falhou! O valor solicitado é inválido.")
    
    elif opcao == "e":
        print("---------------- EXTRATO -----------------")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo: .2f}")
        print("------------------------------------------")

    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor selecione a opção novamente.")

