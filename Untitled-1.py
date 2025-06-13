display = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(display)

    if opcao == "1":
        valor = float(input("Irá depositar?: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito feito com sucesso!")
            print("Deseja fazer outra operação?")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "2":
        valor = float(input("Qual o saque?: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("FALHA! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("FALHA! Valor alto demais.")

        elif excedeu_saques:
            print("FALHA! Chega de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso!")
            print("Deseja fazer outra operação?")
        else:
            print("FALHA! Revise o valor inserido.")

    elif opcao == "3":
        print("\n.......... EXTRATO ..........")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("...............................")
        
    elif opcao == "0":
        break

    else:
        print("Operação inválida, atente-se aos símbolos do display.")