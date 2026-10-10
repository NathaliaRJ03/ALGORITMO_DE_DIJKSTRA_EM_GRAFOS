 Algoritmo de Dijkstra em Grafos (Orientados e Não Orientados)

Este repositório contém implementações em Python do algoritmo de Dijkstra para a determinação dos caminhos mais curtos em grafos ponderados com pesos não negativos.

---

## 📁 Arquivos do Projeto

* **`GRAFO_NAO_ORIENTADO.py`**: Implementação do algoritmo de Dijkstra para grafos não orientados, onde as conexões entre vértices são bidirecionais.
* **`GRAFO_ORIENTADO.py`**: Implementação do algoritmo de Dijkstra para grafos orientados (dígrafos), com validações de entrada interativas e tratamento de erros.

---
## 🛠️ Funcionalidades

### Grafo Não Orientado (`GRAFO_NAO_ORIENTADO.py`)
* Solicita ao usuário a quantidade e o nome de cada vértice.
* Solicita a quantidade de arestas, juntamente com a origem, o destino e o peso.
* Registra as arestas de forma bidirecional no grafo.
* Executa a função `dijkstra` utilizando uma fila de prioridade (`heapq`).
* Exibe a menor distância do vértice inicial para todos os outros vértices conectados.

### Grafo Orientado (`GRAFO_ORIENTADO.py`)
* Valida as entradas numéricas através da função personalizada `ler_inteiro`, evitando falhas na execução.
* Impede a criação de vértices sem nome ou com nomes duplicados.
* Verifica se os vértices de origem e destino existem antes de registrar uma nova aresta.
* Registra as arestas de forma unidirecional e impede o cadastro de arestas duplicadas.
* Exibe a estrutura do grafo no console após o preenchimento.
* Calcula as menores distâncias a partir de um vértice inicial e sinaliza vértices inalcançáveis com a mensagem "Sem caminho".
