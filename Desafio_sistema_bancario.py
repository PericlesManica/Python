opcao_menu = 0
extrato = [0.00]
deposito = 0
soma_extrato = 0
quantidade_de_saques = 0

while True:
    print("""
===========MENU============
      1 - Depositar
      2 - Sacar
      3 - Extrato
      4 - Sair
===========================
""")
    opcao_menu = int(input("Informe a opção: "))
    if opcao_menu == 1:
        deposito = float(input("Valor do depósito: R$"))
        if deposito > 0:
            extrato.append(deposito)
            soma_extrato = 0
            for valor in extrato:
                soma_extrato += valor
            print(f"Saldo da conta: R${soma_extrato:.2f}")
        else:
            print("Valor inválido.")
    if opcao_menu == 2:
        saque = float(input("Valor do saque: R$"))
        if saque > 0 and saque <= soma_extrato and quantidade_de_saques < 3 and saque <= 500:
            extrato.append((saque)*(-1))
            print("Retire o dinheiro.")
            soma_extrato = 0
            quantidade_de_saques += 1
            for valor in extrato:
                soma_extrato += valor
            print(f"Saldo da conta: R${soma_extrato:.2f}")
        elif quantidade_de_saques == 3:
            print("Limite máximo de saques = 3.")
        elif saque >500:
            print("Valor máximo de saque = R$500.")
        elif saque > soma_extrato:
            print("Saldo insuficiente.")
        else:
            print("Valor inválido.")
    if opcao_menu == 3: 
        soma_extrato = 0  
        print(f"Saldo inicial   R${extrato[0]:.2f}") 
        for valor in extrato:
            soma_extrato += valor
            if valor > 0:
                print(f"Depósito        R${valor:.2f}")
            if valor < 0:
                inverve_valor = valor * -1
                print(f"Saque          -R${inverve_valor:.2f}")
        print(f"Saldo da conta: R${soma_extrato:.2f}")
    if opcao_menu == 4:
        print("Saindo do sistema.")
        break
    if opcao_menu > 4 or opcao_menu < 0:
        print("Opção inválida, saindo do sistema.")
        break