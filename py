Class Vetorordenado Preco:

def __init__(self, capacidade=5):

self._tamannho = 0

def redimensionar(self):

nova_cap len(self._codigos) * 2

self._codigos.extend([None] * (nova_cap len(self._codigos)))

self._codigos.extend([None] * (nova_cap len(self._precos)))

print(f" [DEBUG] Redimensionado para capacidade (nova_cap}")

def inserir(self, codigo: int, preco: float):

if self. tamannho == len(self._codigos):

self._redimensionar()

pos = 0

while pos< self._tamannho and self._codigos[pos] < codigo: 1 pos += 1

for i in range(self._tamannho, pos, -1):

print(

f"[DEBUG] Movendo do indice {1-1} para {1}: "

f"({self._codigos[1-1]}, {self._precos[i-1]})"
)
self._codigos[i] = self._codigos[i - 1]

self. precos[1] = self._precos[i - 1]

print(f"[DEBUG] Espaço aberto no inicio (pos)")

self._codigos [pos] = codigo

self._precos [pos] = preco

self._tamannho += 1

Exibe o estado atual do vetor (apenas até self._tamanho)

estado [(self. codigos[1], self. precos[1]) for i in range(self._tamanho)]

print("[DEBUG] Inserido ((codigo), (preco)) vetor: (estado":

def remover(self, codigo: int):

Remove o produto com o código especificado.

Desloca elementos à esquerda para preencher o espaço vazio.

idx= self.buscar (codigo) #busca o indice do código ou -1

if idx-1:

print("[DEBUG] Código (codigo) não encontrado para remoção.")

for i in range(self._tamanho):

print("[DEBUG] Comparando indice (1): (self._codigos[i]} com (codigo)")

if self. codigos[i] = codigo:

return 1

return -1

def imprimir(self):

Exibe todos os produtos cadastrados como Lista de tuplas (codigo, preco).

produtos [(self. codigos[i], self. precos [1]) for i in range(self. tamanho)]


def imprimir(self):

Exibe todos os produtos cadastrados cono lista de tuplas (codigo, preca).

produtos [(self. codigos[i], self. precos[1])

for i in range(self._tawanho)]

print("[DEBUG] Produtos cadastrados:", produtos)

class VetorordenadoPreco:

def executar():

vet VetorordenadoPreco()

while True:

entrada input(">").strip().split()

if not entrada:

continue

cmd = entrada[8].upper()

if cmd == "I":

vet.inserir(int(entrada [1]), float(entrada [2]))

elif cmd = "R": vet.remover(int (entrada [1])) elif cmd = "B":

posvet.buscar (int(entrada[1]))

if pos-1:

print(f"Código {entrada [1]} encontrado na posição (pos).")

else:

print("Código (entrada [1]} não encontrado.")

elif cmd = "P":

def executar():

vet.inserir(int (entrada [2]), float(entrada[2]))

elif cmd == "R":

vet.remover(int(entrada [1]))

elif cmd == "B":

posvet.buscar (int (entrada [1]))

if pos1:

print("Código (entrada [1]} encontrado na posição (pos).")

else:

print("Código (entrada(1)} não encontrado.")

elif cmd ==  "P":

vet.imprimir()

elif cmd = "S":

print("Encerrando.")

break

else:

print("Use I <codigo> <preco>, R <codigo>, 8 <codigo>, Pου S.")



If
name="main":
executar()
