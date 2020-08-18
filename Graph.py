from Edge import Edge
from Vertex import Vertex
from prettytable import PrettyTable


class Graph:

    def __init__(self, vertices: [Vertex] = None):
        self.vertices = vertices

    def getVertexByDepthFirst(self, id):
        root = self.vertices[0]
        if id == root.id:
            return root
        else:
            def get(start: Vertex):
                for edge in start.getEdges():
                    if edge.goingTo.id == id:
                        return edge.goingTo
                    else:
                        get(edge.goingTo)
            return get(root)

    def add(self, vertex: Vertex):
        self.vertices.append(vertex)

    def get(self, id) -> Vertex:
        for vertex in self.vertices:
            if vertex.id == id:
                return vertex

    def adjacencyList(self):
        for vertex in self.vertices:
            print('\n', vertex.id, end=': ')
            edje: Edge
            ids = []
            for edje in vertex.getEdges():
                ids.append(edje.goingTo.id)
            print(' -> '.join(ids))

    def adjacencyMatrix(self):
        table = PrettyTable([' '] + [vertex.id for vertex in self.vertices])
        for vertex in self.vertices:
            row = [vertex.id]
            vertexEdges = [i.goingTo for i in vertex.getEdges()]
            for j in self.vertices:
                if j in vertexEdges:
                    row.append('1')
                else:
                    row.append('0')
            table.add_row(row)
        print(table)

    def incidencyMatrix(self):
        edgesLists = [x.getEdges() for x in self.vertices]
        edges = []
        for j in edgesLists:
            ids = [edge.id for edge in edges]
            weights = [edge.weight for edge in edges]
            edges += [k for k in j if (k.id[1], k.id[0]) not in ids and k.weight not in weights ]
        table = PrettyTable([' '] + [i.id for i in edges])

        for vertex in self.vertices:
            row = [vertex.id]
            for edge in edges:
                if  vertex.id in edge.id:
                    row.append('1')
                else:
                    row.append('0')
            table.add_row(row)
        print(table)

    def isComplete(self):
        for vertex in self.vertices:
            othersVertexes = [x for x in self.vertices if x != vertex]
            allEdges = [otherVertex.getEdges() for otherVertex in othersVertexes]
            for edges in allEdges:
                if vertex not in [x.goingTo for x in edges]:
                    return False
        return True

    def removeEdge(self, commingFrom: int, goingTo: int, weight: float = None):
        for vertex in self.vertices:
            if vertex.id == commingFrom:
                for edge in vertex.getEdges():
                    if edge.goingTo.id == goingTo:
                        vertex.getEdges().remove(edge)

    def getEdges(self, id):
        for v in self.vertices:
            if id == v.id:
                return v.getEdges()

    def remove(self, id):
        vertex_to_remove = self.get(id)
        # retirando da lista
        self.vertices.remove(vertex_to_remove)
        # retirando as arestas
        for v in self.vertices:
            self.removeEdge(v.id, id)
        # edgesLists = [x.getEdges() for x in self.vertices]
        # edges = []
        # for j in edgesLists:
        #     edges += [k for k in j if (k.id[1], k.id[0])]
        # [e.goingTo for e in edges].remove(vertex_to_remove)
    # for v in self.vertices:
        #     for e in v.getEdges():
        #         if e.goingTo.id == id:


