from Edge import Edge
from Vertex import Vertex
from prettytable import PrettyTable


class Graph:

    def __init__(self, vertexes: [Vertex] = None):
        self.vertexes = vertexes

    def getVertexByDepthFirst(self, id):
        root = self.vertexes[0]
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
        self.vertexes.append(vertex)

    def getVertex(self, id) -> Vertex:
        for vertex in self.vertexes:
            if vertex.id == id:
                return vertex

    def adjacencyList(self):
        for vertex in self.vertexes:
            print('\n', vertex.id, end=': ')
            edje: Edge
            ids = []
            for edje in vertex.getEdges():
                ids.append(edje.goingTo.id)
            print(' -> '.join(ids))

    def adjacencyMatrix(self):
        table = PrettyTable([' '] + [vertex.id for vertex in self.vertexes])
        for vertex in self.vertexes:
            row = [vertex.id]
            vertexEdges = [i.goingTo for i in vertex.getEdges()]
            for j in self.vertexes:
                if j in vertexEdges:
                    row.append('1')
                else:
                    row.append('0')
            table.add_row(row)
        print(table)

    def incidencyMatrix(self):
        edgesLists = [x.getEdges() for x in self.vertexes]
        edges = []
        for j in edgesLists:
            edgesIds = [l.id for l in edges]
            edges += [k for k in j if (k.id[1], k.id[0]) not in edgesIds]
        table = PrettyTable([' '] + [i.id for i in edges])

        for vertex in self.vertexes:
            row = [vertex.id]
            for edge in edges:
                if  vertex.id in edge.id:
                    row.append('1')
                else:
                    row.append('0')
            table.add_row(row)
        print(table)

    def isComplete(self):
        for vertex in self.vertexes:
            othersVertexes = [x for x in self.vertexes if x != vertex]
            allEdges = [otherVertex.getEdges() for otherVertex in othersVertexes]
            for edges in allEdges:
                if vertex not in [x.goingTo for x in edges]:
                    return False
        return True

    def removeEdge(self, commingFrom: int, goingTo: int, weight: float):
        for vertex in self.vertexes:
            if vertex.id == commingFrom:
                for edge in vertex.getEdges():
                    if edge.goingTo.id == goingTo:
                        vertex.getEdges().remove(edge)


