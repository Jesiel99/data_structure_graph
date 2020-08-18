from Vertex import Vertex
import gc


class Edge:

    def __init__(self, goingTo: Vertex, weight: int = None, id=None):
        self.goingTo = goingTo
        self.weight = weight
        self.id = (int, int)