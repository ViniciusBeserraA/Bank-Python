LIMITE_SAQUE_DIARIO = 3
saldo = 2000
operacoes = []
usuarios = []
usuario = {}
contaCorrente = {}
conta_correntes = []
numero_conta_corrente = 1000

def sacar(valor):
    global saldo, operacao, LIMITE_SAQUE_DIARIO
    if LIMITE_SAQUE_DIARIO == 0:
        print("Limite de saque diário por conta atingido")
        return
    if valor > saldo or valor <= 0:
        print("Valor inválido para saque. Saldo = ", saldo, ". Valor informado = ", saldo ,"\n")
        return
    saldo -= valor
    LIMITE_SAQUE_DIARIO -= 1
    operacao = f"Saque de R${valor} realizado com sucesso. Saldo final = R${saldo}\n"
    operacoes.append(operacao)

def depositar(valor):
    global saldo, operacao
    if valor <= 0:
        print("Valor inválido para depósito.\n")
        return
    saldo += valor
    operacao = f"Depósito de R${valor} realizado com sucesso. Saldo final = R${saldo}\n"
    operacoes.append(operacao)

def extrato():
    global saldo
    print("==== Extrato da Conta ====")
    for op in operacoes:
        print("==", op," == ")
    print("==== Saldo final ==== ")
    print("==== ", "R$", float(saldo), " ==== \n")

def cadastrarUsuario():
    cpf = input("Informe o CPF: ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado em nossa base.\n")
            return

    nome = input("Informe o nome: ")
    endereco = input("Informe o logradouro: ")
    usuario = {"cpf": cpf, "nome": nome, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.\n")

def gerar_numero_conta_corrente():
    global numero_conta_corrente
    numero_conta_corrente += 1
    return numero_conta_corrente

def cadastrarContaCorrente():
    numeroConta = gerar_numero_conta_corrente()
    usuario = input("Vincule a um usuário cadastrado: ")
    
    usuario_encontrado = False
    for u in usuarios:
        if u['cpf'] == usuario:
            usuario_encontrado = True
            break
    
    if not usuario_encontrado:
        print("Usuário não encontrado. Por favor, cadastre o usuário primeiro.")
        return
    
    contaCorrente = {"agencia": "0001", "numeroConta": numeroConta, "usuario": usuario}
    conta_correntes.append(contaCorrente)
    print("Conta corrente criada e vinculada com sucesso.\n")

def listarClientes():
    print("==== Clientes ====")
    for usuario in usuarios:
        print(f"CPF: {usuario['cpf']}, Nome: {usuario['nome']}, Endereço: {usuario['endereco']}")
    print("\n")
def listarContaCorrentes():
    print("==== Contas ====")
    for conta in conta_correntes:
        print(f"Agencia: {conta['agencia']}, Numero da conta: {conta['numeroConta']}, usuario: {conta['usuario']}")
    print("\n")

print("------- Bank Python V1.2 -------")
print("1 - Sacar \n2 - Depositar Valor \n3 - Exibir Extrato\n4 - Cadastrar Cliente\n"
      "5 - Cadastrar conta corrente\n6 - Listar Base de Clientes\n7 - Listar contas correntes\n8 - Sair\n")

while True:
    opcao = int(input("Informe a operação a ser escolhida = "))
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
        cadastrarUsuario()
    elif opcao == 5:
        cadastrarContaCorrente()
    elif opcao == 6:
        listarClientes()
    elif opcao == 7:
        listarContaCorrentes()
    elif opcao == 8:
        print("programa encerrado")
        break
    else:
        print("Operação inválida")