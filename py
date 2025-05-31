
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










.




class Cargo:
    def __init__(self):
        self.salario_bruto = 0.0

    def set_salario_bruto(self, valor):
        self.salario_bruto = valor

    def get_salario_bruto(self):
        return self.salario_bruto


class Departamento:
    def __init__(self):
        self.nome = ""

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome


class Ocorrencia:
    def __init__(self):
        self.mes = 0
        self.ano = 0
        self.tipo = ""  # "acrescimo" ou "desconto"
        self.valor = 0.0
        self.descricao = ""

    def set_dados(self, mes, ano, tipo, valor, descricao):
        self.mes = mes
        self.ano = ano
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao


class Dependente:
    def __init__(self):
        self.data_nascimento = ""

    def set_data_nascimento(self, data):
        self.data_nascimento = data


class Funcionario:
    def __init__(self):
        self.nome = ""
        self.cargo = None
        self.departamento = None
        self.ocorrencias = []
        self.dependentes = []

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_departamento(self, departamento):
        self.departamento = departamento

    def adicionar_ocorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)

    def adicionar_dependente(self, dependente):
        self.dependentes.append(dependente)

    def retornar_dependentes(self):
        for dep in self.dependentes:
            print("Dependente com nascimento em:", dep.data_nascimento)

    def calcular_salario_liquido(self, mes, ano):
        if self.cargo is None:
            print("Funcionário sem cargo.")
            return 0

        salario = self.cargo.get_salario_bruto()
        for o in self.ocorrencias:
            if o.mes == mes and o.ano == ano:
                if o.tipo == "acrescimo":
                    salario = salario + o.valor
                elif o.tipo == "desconto":
                    salario = salario - o.valor

        for dep in self.dependentes:
            salario = salario + 100  # R$ 100 por dependente

        return salario


# Simulação

# Criando cargo
cargo = Cargo()
cargo.set_salario_bruto(3000)

# Criando departamento
departamento = Departamento()
departamento.set_nome("TI")

# Criando funcionário
func = Funcionario()
func.set_nome("João")
func.set_cargo(cargo)
func.set_departamento(departamento)

# Criando e adicionando ocorrências
oc1 = Ocorrencia()
oc1.set_dados(5, 2025, "acrescimo", 200, "Hora extra")
func.adicionar_ocorrencia(oc1)

oc2 = Ocorrencia()
oc2.set_dados(5, 2025, "desconto", 150, "Falta")
func.adicionar_ocorrencia(oc2)

# Criando e adicionando dependentes
dep1 = Dependente()
dep1.set_data_nascimento("2010-01-01")
func.adicionar_dependente(dep1)

dep2 = Dependente()
dep2.set_data_nascimento("2012-05-05")
func.adicionar_dependente(dep2)

# Exibir dependentes
print("Dependentes de", func.get_nome())
func.retornar_dependentes()

# Calcular salário líquido
salario_liquido = func.calcular_salario_liquido(5, 2025)
print("Salário líquido:", salario_liquido)

# Acessar departamento
print("Departamento do funcionário:", func.departamento.get_nome())

