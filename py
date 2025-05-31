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
