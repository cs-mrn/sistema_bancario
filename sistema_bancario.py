menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Operação desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f} \n"
        
        else: 
            print("Falha na operação! O valor informado é inválido ")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print("Falha na operação: saldo insuficiente")
        
        elif excedeu_limite:
            print("Falha na operação: valor mais alto que o limite de saque")
        
        elif excedeu_saques:
            print("Falha na operação: só é possível realizar três saques por dia")   
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1
        
        else:
            print("Impossível concluir a operação: valor informado inválido")
    
    
    elif opcao == "3":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")
    
    elif opcao =="0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")