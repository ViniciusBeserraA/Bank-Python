LIMITE_SAQUE_DIARIO = 3
saldo = 2000
operacoes = []

def sacar(valor):
    global saldo, operacao, LIMITE_SAQUE_DIARIO
    if LIMITE_SAQUE_DIARIO == 0:
        print("Limite de saque diário por conta atingido")
        return
    if valor > saldo or valor <= 0:
        print("Valor inválido para saque. Saldo = ", saldo, ". Valor informado = ", saldo)
        return
    saldo -= valor
    LIMITE_SAQUE_DIARIO -= 1
    operacao = f"Saque de R${valor} realizado com sucesso. Saldo final = R${saldo}"
    operacoes.append(operacao)

def depositar(valor):
    global saldo, operacao
    if valor <= 0:
        print("Valor inválido para depósito.")
        return
    saldo += valor
    operacao = f"Depósito de R${valor} realizado com sucesso. Saldo final = R${saldo}"
    operacoes.append(operacao)

def extrato():
    global saldo
    print("==== Extrato da Conta ====")
    for op in operacoes:
        print("==", op," == ")
    print("==== Saldo final ==== ")
    print("==== ", "R$", float(saldo), " ==== \n")

print("------- Bank Python V1 -------")
print("1 - Sacar \n2 - Depositar Valor \n3 - Exibir Extrato\n4 - Sair\n")

while True:
    opcao = int(input("Informe o que deseja realizar = "))
    if opcao == 1:
        valor = float(input("Informe o valor que deseja sacar = "))
        sacar(valor)
        print(f"Operação realizada com sucesso. Saldo final = R${saldo}\n")
    elif opcao == 2:
        valor = float(input("Informe o valor que deseja depositar = "))
        depositar(valor)
        print(f"Operação realizada com sucesso. Saldo final = R${saldo}\n")
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        print("programa encerrado")
        break
    else:
        print("Operação inválida")