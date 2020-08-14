

class Vertex:

    count = 0

    def __init__(self, object=None):
        self.id = Vertex.count
        self.object = object
        self.__edges = []
        Vertex.count += 1

    def setEdges(self, edges):
        for edge in edges:
            edge.id = (self.id, edge.goingTo.id)
        self.__edges = edges

    def getEdges(self):
        return self.__edges

    def getAdjacents(self):
        return [x.goingTo for x in self.getEdges()]



