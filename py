E1:

class VetorordenadoPreco:
    def __init__(self, capacidade=5):
        self._codigos = [None] * capacidade
        self._precos = [None] * capacidade
        self._tamannho = 0

    def redimensionar(self):
        nova_cap = len(self._codigos) * 2
        self._codigos.extend([None] * (nova_cap - len(self._codigos)))
        self._precos.extend([None] * (nova_cap - len(self._precos)))
        print(f"[DEBUG] Redimensionado para capacidade {nova_cap}")

    def inserir(self, codigo: int, preco: float):
        if self._tamannho == len(self._codigos):
            self.redimensionar()

        pos = 0
        while pos < self._tamannho and self._codigos[pos] < codigo:
            pos += 1

        for i in range(self._tamannho, pos, -1):
            print(f"[DEBUG] Movendo do indice {i-1} para {i}: "
                  f"({self._codigos[i-1]}, {self._precos[i-1]})")
            self._codigos[i] = self._codigos[i - 1]
            self._precos[i] = self._precos[i - 1]

        print(f"[DEBUG] Espaço aberto no índice {pos}")
        self._codigos[pos] = codigo
        self._precos[pos] = preco
        self._tamannho += 1

        estado = [(self._codigos[i], self._precos[i]) for i in range(self._tamannho)]
        print(f"[DEBUG] Inserido ({codigo}, {preco}) vetor: {estado}")

    def remover(self, codigo: int):
        idx = self.buscar(codigo)
        if idx == -1:
            print(f"[DEBUG] Código {codigo} não encontrado para remoção.")
            return

        for i in range(idx, self._tamannho - 1):
            self._codigos[i] = self._codigos[i + 1]
            self._precos[i] = self._precos[i + 1]

        self._tamannho -= 1
        print(f"[DEBUG] Código {codigo} removido.")

    def buscar(self, codigo: int):
        for i in range(self._tamannho):
            print(f"[DEBUG] Comparando indice {i}: {self._codigos[i]} com {codigo}")
            if self._codigos[i] == codigo:
                return i
        return -1

    def imprimir(self):
        produtos = [(self._codigos[i], self._precos[i]) for i in range(self._tamannho)]
        print("[DEBUG] Produtos cadastrados:", produtos)


def executar():
    vet = VetorordenadoPreco()

    while True:
        entrada = input(">").strip().split()
        if not entrada:
            continue

        cmd = entrada[0].upper()

        if cmd == "I":
            vet.inserir(int(entrada[1]), float(entrada[2]))
        elif cmd == "R":
            vet.remover(int(entrada[1]))
        elif cmd == "B":
            pos = vet.buscar(int(entrada[1]))
            if pos != -1:
                print(f"Código {entrada[1]} encontrado na posição {pos}.")
            else:
                print(f"Código {entrada[1]} não encontrado.")
        elif cmd == "P":
            vet.imprimir()
        elif cmd == "S":
            print("Encerrando.")
            break
        else:
            print("Use I <codigo> <preco>, R <codigo>, B <codigo>, P ou S.")


if __name__ == "__main__":
    executar()



E2:

class EstoqueOrdenado:
    def __init__(self, capacidade=5):
        self._codigos = [None] * capacidade
        self._precos = [None] * capacidade
        self._quantidades = [None] * capacidade
        self._qtde = 0

    def _expandir(self):
        nova_cap = len(self._codigos) * 2
        self._codigos.extend([None] * (nova_cap - len(self._codigos)))
        self._precos.extend([None] * (nova_cap - len(self._precos)))
        self._quantidades.extend([None] * (nova_cap - len(self._quantidades)))
        print(f"[DEBUG] Capacidade aumentada para {nova_cap}")

    def localizar(self, cod: int) -> int:
        for i in range(self._qtde):
            print(f"[DEBUG] Verificando {i}: {self._codigos[i]} vs {cod}")
            if self._codigos[i] == cod:
                return i
        return -1

    def adicionar(self, cod: int, preco: float, qtd: int):
        if self._qtde == len(self._codigos):
            self._expandir()

        i = 0
        while i < self._qtde and self._codigos[i] < cod:
            i += 1

        for j in range(self._qtde, i, -1):
            print(f"[DEBUG] Deslocando de {j-1} para {j}: "
                  f"({self._codigos[j-1]}, {self._precos[j-1]}, {self._quantidades[j-1]})")
            self._codigos[j] = self._codigos[j-1]
            self._precos[j] = self._precos[j-1]
            self._quantidades[j] = self._quantidades[j-1]

        print(f"[DEBUG] Inserção na posição {i}")
        self._codigos[i] = cod
        self._precos[i] = preco
        self._quantidades[i] = qtd
        self._qtde += 1

    def excluir(self, cod: int):
        pos = self.localizar(cod)
        if pos == -1:
            print(f"[DEBUG] Código {cod} não está na lista")
            return

        for i in range(pos, self._qtde - 1):
            print(f"[DEBUG] Reposicionando {i+1} -> {i}")
            self._codigos[i] = self._codigos[i+1]
            self._precos[i] = self._precos[i+1]
            self._quantidades[i] = self._quantidades[i+1]

        self._qtde -= 1
        print(f"[DEBUG] Código {cod} removido")

    def movimentar(self, cod: int, varia: int):
        pos = self.localizar(cod)
        if pos == -1:
            print(f"[DEBUG] Código {cod} inexistente para movimentação")
            return

        self._quantidades[pos] += varia
        print(f"[DEBUG] Nova quantidade de {cod}: {self._quantidades[pos]}")

    def total(self) -> float:
        soma = 0.0
        for i in range(self._qtde):
            soma += self._precos[i] * self._quantidades[i]
        print(f"[DEBUG] Estoque total: {soma}")
        return soma

    def listar(self):
        print("[DEBUG] Listagem dos itens:")
        for i in range(self._qtde):
            print(f"  Código: {self._codigos[i]}, Preço: {self._precos[i]}, Quantidade: {self._quantidades[i]}")


def iniciar():
    estoque = EstoqueOrdenado()

    while True:
        entrada = input(">").strip().split()
        if not entrada:
            continue

        comando = entrada[0].upper()

        if comando == "I" and len(entrada) == 4:
            estoque.adicionar(int(entrada[1]), float(entrada[2]), int(entrada[3]))
        elif comando == "R" and len(entrada) == 2:
            estoque.excluir(int(entrada[1]))
        elif comando == "B" and len(entrada) == 2:
            pos = estoque.localizar(int(entrada[1]))
            if pos != -1:
                print(f"Código {entrada[1]} está na posição {pos}")
            else:
                print(f"Código {entrada[1]} não encontrado")
        elif comando == "A" and len(entrada) == 3:
            estoque.movimentar(int(entrada[1]), int(entrada[2]))
        elif comando == "V":
            estoque.total()
        elif comando == "P":
            estoque.listar()
        elif comando == "S":
            print("Encerrado.")
            break
        else:
            print("Comando inválido. Use: I <cod> <preco> <qtd>, R <cod>, B <cod>, A <cod> <delta>, V, P ou S.")


if __name__ == "__main__":
    iniciar()


calcular_valor_total()->ficat

imprimir) None

4. Exibir trace interno em todas as operações de deslocamento, inserção, remoção e atualização de estoque

5. Redimensionar automaticamente as listas quando atingirem a capacidade.

6. Tratar tentativas de buscar, remover ou atualizar produtos inexistentes.

Formato de Interação

I codigos precos quantidade> inserir novo produto

Rcodigo remover produto do cadastro

codigos buscar produto (retorna indice)

codigo «deltas ajustar quantidade (positivo ou negativo)

mostrar valor total de todos os itens em estoque

imprimir lista completa

s-sair

Requisitos

Não usar list, sort()

Incluir docstrings e comentarios inline explicativos em todo o código

Nome do arquivo de entrega: exercicio_53_estoque.py

Critérios de Avaliação

Correta manutenção da ordenação por código em todas as inserções

Funcionamento de inserção, remoção, busca, atualização de estoque e cálculo de valor total.

Trace interno detalhado de cada deslocamento e de cada ajuste de quantidade.

Tratamento robusto de entradas inválidas e de operações sobre códigos não cadastrados
