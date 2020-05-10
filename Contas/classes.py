
class Conta:

    def __init__(self,num_conta,taxa,saldo,banco):
        self.num = num_conta
        self.taxa = taxa
        self.saldo = saldo
        self.banco = banco

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor





class Conta_corrente(Conta):

    def __init__(self,num,taxa,saldo,banco):
        super(Conta_corrente,self).__init__(num,taxa,saldo,banco)

    def atualiza_cc(self):
       self.saldo -= self.taxa

    def getSaldo_corrente(self):
        return self.saldo



class Conta_poupanca(Conta):

    def __init__(self,num,taxa,saldo,banco):
        super(Conta_poupanca,self).__init__(num,taxa,saldo,banco)

    def atualiza_cp(self):
        self.saldo += self.taxa

    def getSaldo_poupanca(self):
        return self.saldo


class Cliente(Conta_corrente,Conta_poupanca):

    def __init__(self,nome,cpf,num,taxa,saldo,banco):
        super(Cliente,self).__init__(num,taxa,saldo,banco)
        self.nome = nome
        self.cpf = cpf







