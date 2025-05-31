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



=====================================


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

        salario += len(self.dependentes) * 100  # R$100 por dependente
        return salario


# Simulação com dados reais

cargo = Cargo(3000)
departamento = Departamento("Engenharia de Software")
func = Funcionario("João", cargo, departamento)

# Adiciona dependentes
func.adicionar_dependente(Dependente("Maria", "2015-06-01"))
func.adicionar_dependente(Dependente("Lucas", "2012-03-10"))

# Adiciona ocorrências
func.adicionar_ocorrencia(Ocorrencia(5, 2025, 'acrescimo', 500, "Bônus de desempenho"))
func.adicionar_ocorrencia(Ocorrencia(5, 2025, 'desconto', 200, "Atraso"))
func.adicionar_ocorrencia(Ocorrencia(4, 2025, 'acrescimo', 1000, "Mês anterior"))  # Ignorado

# Testes e respostas

print("1) Salário líquido do funcionário em 05/2025:")
print(f"R$ {func.calcular_salario_liquido(5, 2025):.2f}")  # Esperado: 3000 + 500 - 200 + (2 * 100) = 3500

print("\n2) Dependentes do funcionário:")
print(func.retornar_dependentes())  # ['Maria', 'Lucas']

print("\n3) Nome do departamento do funcionário:")
print(func.retornar_departamento())  # Engenharia de Software
