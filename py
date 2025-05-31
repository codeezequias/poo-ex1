
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
# Definição das classes com base no diagrama

class Escolaridade:
    def __init__(self, grau):
        self.grau = grau


class Cidade:
    def __init__(self, nome):
        self.nome = nome


class Estado:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade


class Pais:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado


class Grupo:
    def __init__(self, presidente, sede):
        self.presidente = presidente
        self.sede = sede


class Empresa:
    def __init__(self, diretor, grupo):
        self.diretor = diretor
        self.grupo = grupo


class Departamento:
    def __init__(self, chefe):
        self.chefe = chefe


class Filial:
    def __init__(self, departamento):
        self.departamento = departamento


class Funcionario:
    def __init__(self, nome, escolaridade, alocacao, coordena=None):
        self.nome = nome
        self.escolaridade = escolaridade
        self.alocacao = alocacao
        self.coordena = coordena


# Criação dos objetos simulando uma situação real
cidade = Cidade("São Paulo")
estado = Estado("SP", cidade)
pais = Pais("Brasil", estado)

escolar_presidente = Escolaridade("Doutorado")
presidente = Funcionario("Carlos", escolar_presidente, None)

grupo = Grupo(presidente, pais)
empresa = Empresa("Mariana", grupo)

escolar_chefe = Escolaridade("Mestrado")
chefe_departamento = Funcionario("Fernanda", escolar_chefe, None)

departamento = Departamento(chefe_departamento)
filial = Filial(departamento)

escolar_func = Escolaridade("Graduação")
funcionario = Funcionario("João", escolar_func, departamento, coordena=filial)


# Respostas das perguntas

print("1. Escolaridade do presidente de um grupo:")
print(grupo.presidente.escolaridade.grau)  # Doutorado

print("\n2. País de alocação de um funcionário:")
print(grupo.sede.nome)  # Brasil

print("\n3. Estado da filial que um funcionário coordena:")
print(grupo.sede.estado.nome)  # SP

print("\n4. Escolaridade do chefe de um departamento:")
print(departamento.chefe.escolaridade.grau)  # Mestrado

print("\n5. Nome do diretor da empresa de uma filial:")
print(empresa.dir







      =======

class Cargo:
    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto


class Departamento:
    def __init__(self, nome):
        self.nome = nome


class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Dependente(Pessoa):
    def __init__(self, nome, data_nascimento):
        super().__init__(nome)
        self.data_nascimento = data_nascimento


class Ocorrencia:
    def __init__(self, mes, ano, tipo, valor, descricao):
        self.mes = mes
        self.ano = ano
        self.tipo = tipo  # 'acrescimo' ou 'desconto'
        self.valor = valor
        self.descricao = descricao


class Funcionario(Pessoa):
    def __init__(self, nome, cargo, departamento=None):
        super().__init__(nome)
        if not cargo:
            raise Exception("Funcionário deve ter obrigatoriamente um cargo")
        self.cargo = cargo
        self.departamento = departamento  # pode ser None
        self.dependentes = []
        self.ocorrencias = []

    def adicionar_dependente(self, dependente):
        self.dependentes.append(dependente)

    def adicionar_ocorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)

    def retornar_dependentes(self):
        return [d.nome for d in self.dependentes]

    def retornar_departamento(self):
        return self.departamento.nome if self.departamento else "Sem departamento"

    def calcular_salario_liquido(self, mes, ano):
        salario = self.cargo.salario_bruto

        for o in self.ocorrencias:
            if o.mes == mes and o.ano == ano:
                if o.tipo == 'acrescimo':
                    salario += o.valor
                elif o.tipo == 'desconto':
                    salario -= o.valor

        salario +

