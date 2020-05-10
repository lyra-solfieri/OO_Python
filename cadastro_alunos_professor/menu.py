from cadastro_alunos_professor.classes_pessoa_aluno_professor import Aluno
from cadastro_alunos_professor.classes_pessoa_aluno_professor import Professor
nota = []
aluno2 = []
professor2 = []

print("\n1.Cadastrar Aluno"
      "\n2.Cadastrar Professor "
      "\n3.Obter Média do aluno"
      "\n4.Obter informações do Aluno"
      "\n5.Obter informações do professor"
      "\n0.Sair")
flag = True
while(flag):


    x = int(input("Digite a opção: "))

    if x == 1:

        nome = input("Digite o nome do aluno: ")
        cpf = input("Digite o cpf do aluno ")
        data = input("Data de nascimento do aluno (00/00/00) ")
        for i in range(4):
            n = int(input("Digite a {}º  nota: ".format(i+1)))
            nota.append(n)

        aluno = [Aluno(nome, cpf, data, nota)]
        aluno2.append(aluno)

    elif x == 2:
        nome2 = input("Digite o nome do Professor: ")
        cpf2 = input("Digite o cpf do Professor: ")
        data2 = input("Data de nascimento do professor: ")
        salario = float(input("Digite o salário do Professor: "))

        professor = [Professor(nome2,cpf2,data2,salario)]
        professor2.append(professor)

    elif x == 3:
        soma = 0

        for numero in nota:
            soma += numero
        print("Nota final {} ".format(soma/4))
        nota.clear()

    elif x == 4:
       print(aluno2)


    elif x == 5:

        print(professor2)

    else:
        print("Opção inválida. Hasta la vista,baby")
        break




