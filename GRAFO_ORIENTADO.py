import heapq
def dijkstra(grafo, inicio):
    distancias = {v:float('inf') for v in grafo}
    distancias[inicio]=0
    fila = [(0, inicio)]
    while fila:
        distancias_atual, atual = heapq.heappop(fila)
        if distancia_atual > distancia[atual]:
            continue
        for vizinho, peso in grafo[atual]:
            nova_distancia[vizinho] = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila,(nova_distancia, vizinho))
    return distancias



#===============================


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            numero = int(input(mensagem))
            if numero< minimo:
                print(f"Erro! Digite um numero >= {minimo}.")
                continue
            return numero
        except ValueError:
            print("Erro! Digite um numero inteiro.")



grafo = {}
qtd_vertices = ler_inteiro("Quantidade de vertices: ", 1)
for i in range(qtd_vertices):
    while True:
        vertice = input(f"Nome do vertice {i+1}: ").strip()
        if not vertice:
            print("Erro! O nome nao pode ser vazio.")
        elif vertice in grafo:
            print("Erro!Vertice ja cadastrado")

        else:
            grafo[vertice] = []
            break


qtd_arestas = ler_inteiro("Quantidad de arestas: ", 0)
arestas = set()
for i in range(qtd_arestas):

    print(f"\nAresta {i+1}")
    while True:
        origem = input("Origem: ").strip()
        destino = input("Destino ").strip()
        if origem not in grafo:
            print("Erro!, Vertice  de origem nao existe.")
            continue
        if destino not in grafo:
            print("Erro! Vertice de destino não existe.")
            continue

        if (origem, destino) in arestas:
            print("Erro, Est aresta ja foi cadastrada")
            continue

        peso = ler_inteiro("Peso da aresta", 0)

        grafo[origem].append((destino, peso))
        arestas.add((origem, destino))
        break




print("\n ====Grafo Orientado=====")
for vertice, vizinho in grafo. items():
    print(f"{vertice} -> {vizinhos}")



while True:
    inicio = input("\n Vertice inicial: ").strip()
    if inicio in grafo:
        break
    print("Erro!Vertice nao encontrado.")





resultado = dijkstra(grafo, inicio)
print("\n ===MENORES DISTANCIAS======")
for vertice, distancia in resultado.items():
    if distancia == float('inf'):
        print(f"{incio} -> {vertice} = Sem caminho")
    else:
        print (f"{inicio} -> {vertice} = {distancia}")
