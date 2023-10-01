class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def ElementInRange(self, v):
        return v >= 0 and v < self.max_vertex

    def VertexExists(self, v):
        if not self.ElementInRange(v):
            return False
        return self.vertex[v] is not None

    def Capacity(self):
        employmant_vertex_rate = self.max_vertex - self.vertex.count(None)
        return self.max_vertex - employmant_vertex_rate

    def GetFreeIdx(self):
        for Idx in range(self.max_vertex):
            if self.vertex[Idx] is None:
                return Idx
        return None

    def AddVertex(self, v):
        NewVertexIdx = self.GetFreeIdx()
        if NewVertexIdx is None:
            return
        self.vertex[NewVertexIdx] = Vertex(v)
        return NewVertexIdx

    def RemoveVertex(self, v):
        if not self.VertexExists(v):
            return False
        for idx in range(self.max_vertex):
            self.m_adjacency[idx][v] = None
            self.m_adjacency[v][idx] = None
        self.vertex[v] = None
        return True

    def IsEdge(self, v1, v2):
        if not self.VertexExists(v1) or not self.VertexExists(v2):
            return False
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        return False

    def AddEdge(self, v1, v2):
        if not self.VertexExists(v1) or not self.VertexExists(v2):
            return False
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return True

    def RemoveEdge(self, v1, v2):
        if not self.VertexExists(v1) or not self.VertexExists(v2):
            return False
        self.m_adjacency[v1][v2] = None
        self.m_adjacency[v2][v1] = None
        return True
