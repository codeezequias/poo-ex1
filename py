class Departamento:
    def __init__(self):
        self.funcionarios = []
    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    def exibir_funcionarios(self):
        for func in self.funcionarios:
            print(func.get_nome())
    def calcular_folha_pagamento(self):
        total_folha = 0
        for func in self.funcionarios:
            total_folha = total_folha + func.get_salario()
        return total_folha
class Funcionario:
    def __init__(self):
        self.nome = ""
        self.salario = 0.0
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    def set_salario(self, salario):
        self.salario = salario
    def get_salario(self):
        return self.salario

func1 = Funcionario()
func2 = Funcionario()
func1.set_nome("Ana")
func1.set_salario(10000)
func2.set_nome("Maria")
func2.set_salario(5000)
depto1 = Departamento()
depto1.contratar_funcionario(func1)
depto1.contratar_funcionario(func2)
depto1.exibir_funcionarios()
total = depto1.calcular_folha_pagamento()
print(f"Folha pagamento = {total:.2f}")

func3 = Funcionario()
func3.set_nome("Amanda")
func3.set_salario(1200.0)
func4 = Funcionario()
func4.set_nome("Mirella")
func4.set_salario(2400.0)
func5 = Funcionario()
func5.set_nome("Rafaela")
func5.set_salario(2400.0)
depto2 = Departamento()
depto2.contratar_funcionario(func3)
depto2.contratar_funcionario(func4)
depto2.contratar_funcionario(func5)
depto2.exibir_funcionarios()
total2 = depto2.calcular_folha_pagamento()
print(f"Folha pagamento = {total2:.2f}")
