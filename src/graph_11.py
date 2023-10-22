import queue


class SimpleTreeNode:

    def __init__(self, val, parent=None):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def __repr__(self):
        return f"(Node UID: {id(self)}. Value: {self.NodeValue})"

    def __str__(self):
        return self.__repr__()

    @property
    def IsLeaf(self):
        return len(self.Children) == 0


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        # ваш код добавления нового дочернего узла существующему ParentNode
        Nodes = self.FindNodesByValue(ParentNode.NodeValue)
        if len(Nodes) == 0:
            return
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        """ваш код удаления существующего узла NodeToDelete"""
        self._RemoveNodeFromParent(NodeToDelete)
        self._RemoveChildrenFromNode(NodeToDelete)

    def GetPathToRoot(self, Node: SimpleTreeNode):
        if Node is None:
            return []
        ListOfNodes = []
        PathWasFound = self._GetPathToRoot(Node, ListOfNodes)
        return ListOfNodes if PathWasFound else None

    def _GetPathToRoot(self, Node, ListOfNodes):
        ListOfNodes.append(Node.NodeValue)
        ParentNode = Node.Parent
        if ParentNode is None:
            if self.Root == Node:
                return True
            else:
                return False
        return self._GetPathToRoot(ParentNode, ListOfNodes)

    def _RemoveNodeFromParent(self, NodeToDelete: SimpleTreeNode):
        ParentNode = NodeToDelete.Parent
        Node_Index = None
        for Node_Index, Node in enumerate(ParentNode.Children):
            if Node == NodeToDelete:
                break
        if Node_Index is not None:
            ParentNode.Children.pop(Node_Index)

    def _RemoveChildrenFromNode(self, NodeToDelete: SimpleTreeNode):
        NodeToDelete.Children = []

    def GetAllNodes(self):
        """
        ваш код выдачи всех узлов дерева в определённом порядке

        Формат выдачи:
        [
            {
                "Node_Root": [
                    {"Node_A": [
                        {"Node_A_1": []},
                        {"Node_A_2": []},
                        {"Node_A_3": []}
                    ]},
                    {"Node_B": []},
                    {"Node_C": []}
                ]
            }
        ]
        """
        NodesList = []
        self._TraverseTheTree(self.Root, NodesList)
        return NodesList

    def _TraverseTheTree(self, Node: SimpleTreeNode, NodesList: list):
        NodesList.append(Node)
        if Node.IsLeaf:
            return None
        else:
            for ChildNode in Node.Children:
                self._TraverseTheTree(ChildNode, NodesList)

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        ResultsList = []
        self._FindNodes(ResultsList, self.Root, val)
        return ResultsList

    def _FindNodes(self, ResultsList, Node: SimpleTreeNode, val):
        if Node.NodeValue == val:
            ResultsList.append(Node)

        ChildNodes = Node.Children
        if len(ChildNodes) == 0:
            return

        for ChildNode in ChildNodes:
            self._FindNodes(ResultsList, ChildNode, val)

        return

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        """
        код перемещения узла вместе с его поддеревом --
        в качестве дочернего для узла NewParent
        """
        self._RemoveNodeFromParent(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)

    def Count(self):
        """количество всех узлов в дереве"""
        result = self._Count(self.Root)
        return result

    def _Count(self, Node: SimpleTreeNode):
        return len(self.GetAllNodes())

    def LeafCount(self):
        # количество листьев в дереве
        return self._LeafCount(self.Root)

    def _LeafCount(self, Node: SimpleTreeNode):
        ChildNodes = Node.Children

        if len(ChildNodes) == 0:
            return 1

        accumulator = 0

        for ChildNode in ChildNodes:
            accumulator += self._LeafCount(ChildNode)

        return accumulator

    def EvenTrees(self):
        ListOfRemovingNodes = []
        if self.Root is None:
            return ListOfRemovingNodes
        self._EvenTrees(self.Root, ListOfRemovingNodes)
        return ListOfRemovingNodes

    def _EvenTrees(self, Node: SimpleTreeNode, ListOfRemovingNodes: list):
        NodesAmount = 1
        if Node.IsLeaf:
            return NodesAmount
        for ChildNode in Node.Children:
            NodesAmount += self._EvenTrees(ChildNode, ListOfRemovingNodes)
        if NodesAmount != 0 and NodesAmount % 2 == 0 and Node.Parent is not None:
            ListOfRemovingNodes.append(Node.Parent)
            ListOfRemovingNodes.append(Node)
        return NodesAmount


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

        self._PathTree = SimpleTree(None)

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

    def _UnhitVertices(self):
        for Item in self.vertex:
            if Item is None:
                continue
            Item.Hit = False

    def _ClearBeforeDeepFirstSearch(self):
        self.stack = []
        self._UnhitVertices()

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
        self._ClearBeforeDeepFirstSearch()
        self._ProcessDFS(VFrom, VTo)
        return [self.vertex[i] for i in self.stack]

    def _ProcessDFS(self, VFrom: int, VTo: int):
        self.vertex[VFrom].Hit = True
        self.stack.append(VFrom)

        AdjacentVertexIndexes = self._GetAdjacentVertexIndexes(VFrom)

        for VIdx in AdjacentVertexIndexes:
            if VIdx == VTo:
                self.stack.append(VIdx)
                return True
            if self.vertex[VIdx].Hit is False:
                WasFound = self._ProcessDFS(VIdx, VTo)
                if WasFound:
                    return True

        self.stack.pop()

        return False

    def BreadthFirstSearch(self, VFrom: int, VTo: int):
        try:
            self._UnhitVertices()

            if (VFrom is None or self.vertex[VFrom] is None) or (VTo is None or self.vertex[VTo] is None):
                return None

            RootNode = SimpleTreeNode(VFrom)
            self._PathTree.Root = RootNode

            AdjacentVerticesQueue = queue.Queue()

            self.vertex[VFrom].Hit = True
            result = self._ProcessBFS(RootNode, VTo, AdjacentVerticesQueue)

            if result is not None:
                Path = self._PathTree.GetPathToRoot(result)
                return [Vertex(VIdx) for VIdx in reversed(Path)]

            return None

        finally:
            self._PathTree = SimpleTree(None)

    def _ProcessBFS(self, VFromNode, VToValue, AdjacentVerticesQueue) -> SimpleTreeNode:
        VFromValue = VFromNode.NodeValue
        AdjacentVertexIndexes = self._GetAdjacentVertexIndexes(VFromValue)

        for VIdx in AdjacentVertexIndexes:
            CurrentPathNode = SimpleTreeNode(VIdx)
            self._PathTree.AddChild(VFromNode, CurrentPathNode)
            if VIdx == VToValue:
                return CurrentPathNode
            self.vertex[VIdx].Hit = True
            AdjacentVerticesQueue.put(CurrentPathNode)

        try:
            NewVFromNode = AdjacentVerticesQueue.get_nowait()
            return self._ProcessBFS(NewVFromNode, VToValue, AdjacentVerticesQueue)
        except queue.Empty:
            return None
