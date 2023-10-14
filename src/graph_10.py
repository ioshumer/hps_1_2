class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

    def __repr__(self):
        return str(self.Value)

    def __str__(self):
        return str(self.Value)


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.stack = []

    def _VertexExists(self, v):
        IsElementInRange = v >= 0 and v < self.max_vertex
        if not IsElementInRange:
            return False
        return self.vertex[v] is not None

    def _GetFreeIdx(self):
        for Idx in range(self.max_vertex):
            if self.vertex[Idx] is None:
                return Idx
        return None

    def AddVertex(self, v):
        NewVertexIdx = self._GetFreeIdx()
        if NewVertexIdx is None:
            return
        self.vertex[NewVertexIdx] = Vertex(v)
        return NewVertexIdx

    def RemoveVertex(self, v):
        if not self._VertexExists(v):
            return False
        for idx in range(self.max_vertex):
            self.m_adjacency[idx][v] = None
            self.m_adjacency[v][idx] = None
        self.vertex[v] = None
        return True

    def IsEdge(self, v1, v2):
        if not self._VertexExists(v1) or not self._VertexExists(v2):
            return False

        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True

        return False

    def AddEdge(self, v1, v2):
        if not self._VertexExists(v1) or not self._VertexExists(v2):
            return False
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        return True

    def RemoveEdge(self, v1, v2):
        if not self._VertexExists(v1) or not self._VertexExists(v2):
            return False
        self.m_adjacency[v1][v2] = None
        self.m_adjacency[v2][v1] = None
        return True

    def _ClearBeforeDeepFirstSearch(self):
        self.stack = []
        for Item in self.vertex:
            if Item is None:
                continue
            Item.Hit = False

    def _GetAdjacentVertexIndexes(self, VertexIdx: int):

        VertexMapping = self.m_adjacency[VertexIdx]
        AdjacentVerteces = []
        IsMappedSign = 1

        for Pointer, Value in enumerate(VertexMapping):
            CurrentVertex = self.vertex[Pointer]
            WasHit = False if CurrentVertex is None else CurrentVertex.Hit
            if Value == IsMappedSign and Pointer != VertexIdx and not WasHit:
                AdjacentVerteces.append(Pointer)

        return AdjacentVerteces

    def DepthFirstSearch(self, VFrom: int, VTo: int):
        if not self._VertexExists(VFrom) or not self._VertexExists(VTo):
            return []
        self._Process(VFrom, VTo)
        return [self.vertex[i] for i in self.stack]

    def _Process(self, VFrom: int, VTo: int):

        self.vertex[VFrom].Hit = True
        self.stack.append(VFrom)

        AdjacentVertexIndexes = self._GetAdjacentVertexIndexes(VFrom)

        for VIdx in AdjacentVertexIndexes:
            if VIdx == VTo:
                self.stack.append(VIdx)
                return True

        # for VIdx in AdjacentVertexIndexes:
            if self.vertex[VIdx].Hit is False:
                WasFound = self._Process(VIdx, VTo)
                if WasFound:
                    return True

        self.stack.pop()

        return False
