class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла

    @property
    def IsLeaf(self):
        return self.LeftChild is None and self.RightChild is None


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def _PrepareArray(self, Array):
        CopiedArray = Array.copy()
        CopiedArray.sort()
        return CopiedArray

    def _BuildNode(self, Key, Parent=None, LeftChild=None, RightChild=None, Level=None):
        NewNode = BSTNode(Key, Parent)
        NewNode.LeftChild = LeftChild
        NewNode.RightChild = RightChild
        NewNode.Level = Level
        return NewNode

    def _PrepareVertexNode(self, VertexIndex, Parent=None, Level=None):
        VertexKey = self._SortedArray[VertexIndex]
        VertexNode = self._BuildNode(VertexKey, Parent, Level=Level)
        return VertexNode

    def _DefineVertexIndex(self, LeftBound, RightBound):
        Delta = ((RightBound - LeftBound) + 1) // 2
        return LeftBound + Delta

    def GenerateTree(self, a):
        ArrayLength = len(a)
        if ArrayLength == 0:
            return
        self._SortedArray = self._PrepareArray(a)

        LeftBound = 0
        RightBound = ArrayLength - 1
        CurrentTreeLevel = 0

        ArrayLength = len(self._SortedArray[LeftBound:RightBound + 1])

        VertexIndex = self._DefineVertexIndex(LeftBound, RightBound)
        RootNode = self._PrepareVertexNode(VertexIndex, Level=CurrentTreeLevel)

        self.Root = RootNode

        if ArrayLength == 1:
            return

        RootNode.LeftChild = self._RecursiveProcessing(RootNode, LeftBound, VertexIndex - 1, CurrentTreeLevel)
        RootNode.RightChild = self._RecursiveProcessing(RootNode, VertexIndex + 1, RightBound, CurrentTreeLevel)

    def _RecursiveProcessing(self, ParentNode: BSTNode, LeftBound: int, RightBound: int, Level: int):
        if LeftBound > RightBound:
            return

        CurrentTreeLevel = Level + 1
        VertexIndex = self._DefineVertexIndex(LeftBound, RightBound)
        VertexNode = self._PrepareVertexNode(VertexIndex, Parent=ParentNode, Level=CurrentTreeLevel)

        if VertexNode is None:
            return

        IsLeaf = RightBound == LeftBound
        if IsLeaf:
            return VertexNode

        LeftNode = self._RecursiveProcessing(VertexNode, LeftBound, VertexIndex - 1, CurrentTreeLevel)
        RightNode = self._RecursiveProcessing(VertexNode, VertexIndex + 1, RightBound, CurrentTreeLevel)

        if LeftNode:
            VertexNode.LeftChild = LeftNode
        if RightNode:
            VertexNode.RightChild = RightNode

        return VertexNode

    def IsBalanced(self, root_node: BSTNode):
        if self.Root is None:
            return True
        if root_node.LeftChild is not None:
            LeftSubtreeDepth = self._GetDepthOfSubtree(root_node.LeftChild)
        else:
            LeftSubtreeDepth = 0

        if root_node.RightChild is not None:
            RightSubtreeDepth = self._GetDepthOfSubtree(root_node.RightChild)
        else:
            RightSubtreeDepth = 0

        BalanceSign = abs(LeftSubtreeDepth - RightSubtreeDepth) <= 1
        return BalanceSign

    def _GetDepthOfSubtree(self, Node: BSTNode):
        if Node.IsLeaf:
            return Node.Level

        if Node.LeftChild is None:
            LeftChildLevel = 0
        else:
            LeftChildLevel = self._GetDepthOfSubtree(Node.LeftChild)

        if Node.RightChild is None:
            RightChildLevel = 0
        else:
            RightChildLevel = self._GetDepthOfSubtree(Node.RightChild)

        return max(LeftChildLevel, RightChildLevel)
