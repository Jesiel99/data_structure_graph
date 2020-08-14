from Edge import Edge
from Graph import Graph
from Vertex import Vertex


def isEdgesEmpty(vertex: Vertex):
    if vertex.getEdges() is None:
        return True
    else:
        return False

laurentino = Vertex('laurentino')
rioDoSul = Vertex('rio do sul')
rioDoOeste = Vertex('rio do oeste')

rioDoOeste.setEdges([Edge(laurentino, 3)])
rioDoSul.setEdges([Edge(laurentino, 4)])
laurentino.setEdges([Edge(rioDoSul, 2)])

graph = Graph([laurentino, rioDoSul, rioDoOeste])
#graph = Graph([laurentino, rioDoSul])

# c
print('--------------remoção----------------')
graph.removeEdge(1, 0, 1)
graph.adjacencyMatrix()
# d
print('--------lista de adjacências---------')
vertexes = [x.object for x in graph.getVertex(0).getAdjacents()]
print(vertexes)
# e
print('---vertice 1 está sem adjacências?---')
print(isEdgesEmpty(graph.getVertex(1)))
# f
print('--------matriz de incidência?--------')
graph.incidencyMatrix()
# g
print('---------é um grafo completo?--------')
print(graph.isComplete())
# h
print('---------busca em largura--------')
print(graph.getVertexByDepthFirst(0).object)
print('---------busca em profundidade--------')
print(graph.getVertex(0).object)
