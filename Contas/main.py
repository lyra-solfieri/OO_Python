from Contas.classes import Cliente

global cliente1


print('\n1.Cadastrar Cliente (Incluindo Conta corrente e Poupança) '
      '\n2.Saque da conta corrente(Procurar pelo CPF do Cliente)'
      '\n3.Saque da poupança(Procurar pelo CPF do Cliente)'
      '\n4.Depósito da conta corrente(Procurar pelo CPF do Cliente)'
      '\n5.Depósito da poupança(Procurar pelo CPF do Cliente)'
      '\n0.Sair')
loop = True

while(loop):
    x = int(input('Digite a opção: '))

    if x == 1:
        nome = input('Digite o nome do cliente: ')
        cpf = input('Digite o cpf do Cliente ')
        num = input('Digite o número da conta: ')
        taxa = float(input('Digite a taxa fixa: '))
        saldo = float(input('Digite o saldo: '))
        banco = input('Digite o banco: ')

        cliente1 = Cliente(nome,cpf,num,taxa,saldo,banco)
        print(vars(cliente1))


    elif x == 2:
       print('Sacar da conta corrente ')
       cpf2 = input('Digite o cpf para sacar:')
       if cliente1.cpf == cpf2:
           valor = float(input('Digite o valor para sacar: '))
           cliente1.sacar(valor)
           cliente1.atualiza_cc()
           print('saldo atual :', cliente1.getSaldo_corrente())
       else:
           print('Opção inválida')

    elif x == 3:
        print('Sacar da conta poupança ')
        cpf3 = input('Digite o cpf para sacar:')
        if cliente1.cpf == cpf3:
            valor = float(input('Digite o valor para sacar: '))
            cliente1.sacar(valor)
            cliente1.atualiza_cp()
            print('saldo atual: ', cliente1.getSaldo_poupanca())
        else:
            print('Opção inválida')

    elif x == 4:
        print('Depositar na conta corrente')
        cpf4 = input('Digite o cpf correto: ')
        if cliente1.cpf == cpf4:
            v = float(input(' Digite o valor '))
            cliente1.depositar(v)
            print('Saldo atual: ', cliente1.getSaldo_corrente())
        else:
            print('Opção inválida')

    elif x == 5:
        print('Depositar na conta poupança')
        cpf5 = input('Digite o cpf correto: ')
        if cliente1.cpf == cpf5:
            v2 = float(input(' Digite o valor '))
            cliente1.depositar(v2)
            print('Saldo atual: ', cliente1.getSaldo_poupanca())
        else:
            print('Opção inválida')

    else:
        print('Ô loco bicho tu digitou errado, hasta la vista')
        break

