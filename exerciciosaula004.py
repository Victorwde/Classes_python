
class Turma():
    def __init__(self,diciplina,ano,professor,alunos):
        self.diciplina = diciplina
        self.ano = ano
        self.professor = professor
        self.alunos = alunos

class Professor():
    def __init__(self,nome1):
        self.nome1 = nome1

class Aluno():
    def __init__(self,nome2):
        self.nome2 = nome2

turma = Turma('Programação Orientada a Objetos','2022','Marcus Vasconcelos','Alunos')
print(turma.diciplina,'/',turma.ano,'/',turma.professor,'/',turma.alunos)
prof = Professor(str(input('Digite o nome do professor:')))
alun = Aluno('Aluno: Victor Souza')
print('Professor: ',prof.nome1)
print(alun.nome2)