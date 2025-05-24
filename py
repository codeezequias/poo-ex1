
class Escolaridade:
    def __init__(self):
        self.nome = ""
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

class Funcionario:
    def __init__(self, escolaridade):
        self.set_escolaridade(escolaridade)
    def set_escolaridade(self, escolaridade):
        if escolaridade == None:
            print("Escolaridade invalida")
        else:
            self.escolaridade = escolaridade
    def get_escolaridade(self):
        return self.escolaridade
    def get_nome_escolaridade(self):
        return self.escolaridade.get_nome()

class Grupo:
    def __init__(self):
        self.presidente = None
    def get_presidente(self):
        return self.presidente
    def set_presidente(self, presidente):
        self.presidente = presidente
    def get_nome_escolaridade_presidente(self):
        if self.presidente == None:
            return "Grupo sem presidente"
        else:
            return self.presidente.get_nome_escolaridade()

escolaridade = Escolaridade()
escolaridade.set_nome("Graduacao")
presidente = Funcionario(escolaridade)
grupo = Grupo()
grupo.set_presidente(presidente)
print(grupo.get_nome_escolaridade_presidente())



def __init__(self):
        self.turmas = []

    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def exibir_professores_do_curso(self):
        print("Professores que lecionam neste curso:")
        for turma in self.turmas:
            professor = turma.get_professor()
            if professor:
                print(professor.get_nome())
