class Aluno:
    def __init__(self, nome, CPF, endereco, curso):
        self.nome = nome
        self.CPF = CPF
        self.endereco = endereco
        self.curso = curso
        
    def __str__(self):
        return f"Aluno: {self.nome}, CPF: {self.CPF}, Endereco: {self.endereco.cidade}, {self.endereco.bairro}, {self.endereco.rua}, {self.endereco.numero}, Curso: {self.curso.nome}"
    

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunosCurso = []

    def addAlunoCurso (self, aluno):
        self.alunosCurso.append(aluno)
    
    def mostraALunosCurso(self):
        print("\n---CURSO---")
        print("Nome do curso: ", self.nome)
        for aluno in self.alunosCurso:
            print(aluno.nome,)
        print("---------------")


class Endereco:
    def __init__(self, cidade, bairro, rua, numero):
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

        
class Disciplina:
    def __init__(self, nome, professor, bloco, sala):
        self.nome = nome
        self.professor = professor
        self.bloco = bloco
        self.sala = sala
        self.alunosSala = []

    def adicionarAlunosNaSala (self, aluno):
        self.alunosSala.append(aluno)
    
    def mostrarParticipantesSala(self):
        print("\n--DISCIPLINA--")
        print(self.nome)
        print("Professor:", self.professor)
        print("Sala:", self.sala)
        print("\nAlunos:")
        for aluno in self.alunosSala:
            print(aluno.nome)
        print("---------------")



enderecoAluno1 = Endereco("Flores", "Centro", "Rua2", 111)
aluno1 = Aluno("Gumercindo", "000.000.000-00", enderecoAluno1, None)

enderecoAluno2 = Endereco("Flores", "Centro", "Rua 3", 222)
aluno2 = Aluno("Fernanda", "111.111.111-11", enderecoAluno2, None)

enderecoAluno3 = Endereco("Flores", "Centro", "Rua 4", 333)
aluno3 = Aluno("Rafael", "222.222.222-22", enderecoAluno3, None)

enderecoAluno4 = Endereco("Flores", "Centro", "Rua 5", 444)
aluno4 = Aluno("Juliana", "333.333.333-33", enderecoAluno4, None)

enderecoAluno5 = Endereco("Flores", "Centro", "Rua 6", 555)
aluno5 = Aluno("Pedro", "444.444.444-44", enderecoAluno5, None)

sistamaInformacao = Curso("Sistemas de Informação")
sistamaInformacao.addAlunoCurso(aluno1)
sistamaInformacao.addAlunoCurso(aluno2)

quimica = Curso("Quimica")
quimica.addAlunoCurso(aluno3)
quimica.addAlunoCurso(aluno4)
quimica.addAlunoCurso(aluno5)

sistamaInformacao.mostraALunosCurso()
quimica.mostraALunosCurso()


mpoo = Disciplina("MPOO","Napoleon", 1, 13)
mpoo.adicionarAlunosNaSala(aluno1)
mpoo.adicionarAlunosNaSala(aluno2)

algebra = Disciplina("Algebra", "Abel", 3, 12)

algebra.adicionarAlunosNaSala(aluno1)
algebra.adicionarAlunosNaSala(aluno3)
algebra.adicionarAlunosNaSala(aluno4)
algebra.adicionarAlunosNaSala(aluno5)


mpoo.mostrarParticipantesSala()
algebra.mostrarParticipantesSala()