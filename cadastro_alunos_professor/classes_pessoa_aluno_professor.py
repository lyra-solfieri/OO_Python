class Pessoa:
    def __init__(self,nome,cpf,data):
        super(Pessoa,self).__init__()
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data

    def __str__(self):

        return str(self.nome,self.cpf,self.data_nascimento)

class Aluno(Pessoa):

   def __init__(self,nome,cpf,data,nota):
       super(Aluno,self).__init__(nome,cpf,data)
       self.nota = nota

   def __float__(self,n):
       return float(self.nota[n])

   def __repr__(self):
       return str(self.__dict__)
   def __eq__(self, other):
       return self.__dict__ == other.__dict__


class Professor(Pessoa):

    def __init__(self,nome,cpf,data,salario):
        super(Professor,self).__init__(nome, cpf,data)
        self.salario = salario

    def __float__(self):
        return float(self.salario)

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

