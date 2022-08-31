class Aluno:
    def __init__(self,matricula,curso,periodo):
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo

    def cadastrarAluno(self,matricula,curso,periodo):
        self.matricula = matricula
        matricula = input ("Matricula:")
             
        self.curso = curso
        curso = input("Curso: ")

        self.periodo = periodo
        periodo = input ("Periodo:")
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo
        
    def relatorioAluno(self):
        print(f' matricula: {self.matricula}\n Curso: {self.curso}\n Periodo: \t{self.periodo}')
    

    def alterarAlunos(self,matricula,curso,periodo):
        self.matricula = matricula
        matricula = input ("Matricula:")
             
        self.curso = curso
        curso = input("Curso: ")

        self.periodo = periodo
        periodo = input ("Periodo:")

        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo
    
    def excluirAluno(self):
        self.matricula = ' '
        self.curso = ' '
        self.periodo = ' '
        