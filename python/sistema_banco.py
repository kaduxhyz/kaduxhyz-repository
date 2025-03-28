#print("**********Menu**********")
#print("Criar Usuario")
#print("Depositar")
#print("Sacar")]

#criei uma lista vazia, pois serão adicionados valores posteriormente
saldo = 0
numere_saques = 0
limites = 500
limites_saques = 3
usuario = []
contas = []
agencia = '001'


def menu():
    print('''
        **********Menu**********
        (1) Criar Usuario
        (2) Criar Conta
        (3) Listar Contas
        (d) Depositar
        (s) Sacar
        (e) Estrato
        (q) Sair
    ''')
    return input("Qual opção deseja?")
menu()

def deposito(valor,saldo):
    # valor receber o valor do deposito e somar o saldo
    if valor >0 :
        saldo += valor
        #print mostrando o valor depositado
        print(f'Voce depositou R${valor}')

    else:
        print('Valor do deposito Invalido. Verifique a quantia digitada.')

    return saldo

def saque(saque,saldo):
    global numere_saques,limites,limites_saques
    #de acordo com a documentação Python, variaveis globais não ficam ao limite do escopo da função.
    if numere_saques >= limites_saques
    print('Você atingiu o limite de saques da sua conta, Tente novamente ou no proximo dia útil')

    else:
        if saque <= 0:
            print('Saque inválido. Veirfique o valor e tente novamente.')
        elif saque > limites : 
            print('valor limite excedido. Verifique o valor e tente novamente.')
        elif saque saldo :
            print('Saldo insuficiente. Verifique o valor e tente novamente.')
        else :
            saldo -= saque
            numere_saques += 1
        return saldo