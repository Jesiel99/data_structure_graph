from Edge import Edge
from Graph import Graph
from Vertex import Vertex
import multiprocessing as mp


def isEdgesEmpty(vertex: Vertex):
    if vertex.getEdges() is None:
        return True
    else:
        return False


def isEuloriano(graph: Graph):
    pairs = [vertex.getEdges() for vertex in graph.vertices if len(vertex.getEdges()) / 2 == 0]
    if len(pairs) == len(graph.vertices):
        print('Euleriano')
    elif len(pairs) == 0:
        print('Não Euleriano')
    else:
        print('Semi-Euleriano')


def isHamiltonian(vertices: [Vertex], root: Vertex):
    goneTo = [root]

    def isIt(start: Vertex):
        #pega todos os vertices
        for vertex in [v.goingTo for v in start.getEdges()]:
            # se já passou por todos os vertices
            if len(goneTo) == len(vertices):
                if root == vertex:
                    return 'Hamiltoniano'
                return 'Semi-Hamiltoniano'
            # se já foi passado pelo cértice
            elif vertex not in goneTo:
                goneTo.append(vertex)
                return isIt(vertex)

    return isIt(root) or 'Não hamiltoniano'

laurentino = Vertex('laurentino')
rioDoSul = Vertex('rio do sul')
rioDoOeste = Vertex('rio do oeste')

# hamiltoniano
laurentino.setEdges([Edge(rioDoSul, 2)])
rioDoSul.setEdges([Edge(rioDoOeste, 4)])
rioDoOeste.setEdges([Edge(laurentino, 3)])
# semi
# laurentino.setEdges([Edge(rioDoSul, 2)])
# rioDoSul.setEdges([Edge(rioDoOeste, 4)])
# rioDoOeste.setEdges([Edge(rioDoOeste, 4)])
# #nao
# laurentino.setEdges([Edge(rioDoSul, 2)])
# rioDoSul.setEdges([Edge(laurentino, 4)])
# rioDoOeste.setEdges([Edge(rioDoOeste, 4)])

# rioDoSul.setEdges([Edge(laurentino, 4)])

graph = Graph([laurentino, rioDoSul, rioDoOeste])

print('Exercício 3:')

# 3 d
print('--------lista de adjacências---------')
print([x.object for x in graph.get(0).getAdjacents()])
# 3 e
print('---vertice 1 está sem adjacências?---')
print(isEdgesEmpty(graph.get(1)))
# 3 f
print('--------matriz de incidência?--------')
graph.incidencyMatrix()
# 3 g
print('---------é um grafo completo?--------')
print(graph.isComplete())
# 3 h
print('-----------busca em largura----------')
print(graph.getVertexByDepthFirst(0).object)
print('---------busca em profundidade-------')
print(graph.get(0).object)
# 4.2
print('------------É Euleriano?-------------')
isEuloriano(graph)
print('-----------É Hamiltoniano------------')
print(isHamiltonian(graph.vertices, graph.vertices[0]))
# 3 c
print('--------------remoção----------------')
graph.remove(1)
graph.adjacencyMatrix()