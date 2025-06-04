Contexto

A partir da mesma ideia de manter produtos em um vetor ordenado por código, agora cada item tem preço e quantidade em estoque. Seu programa deve permitir controle de entradas e saldas de estoque, além de relatórios de valor total

Objetivos

1. Adaptar a estrutura para três listas paralelas: códigos, preços e quantidades

2. Manter a ordenação crescente por código a cada inserção.

3. Implementar os métodos:

inseriricodigo: int, preco: float, quantidade: int)

remover codigo: int)

buscar codigo: int) int

atualizar estoque(codigo: int, delta: int)

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
