class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent: BSTNode = parent  # родитель или None для корня
        self.LeftChild: BSTNode = None  # левый потомок
        self.RightChild: BSTNode = None  # правый потомок

    @property
    def HasLeftChild(self):
        return self.LeftChild is not None

    @property
    def HasRightChild(self):
        return self.RightChild is not None

    @property
    def HasBothChildren(self):
        return self.HasLeftChild and self.HasRightChild

    @property
    def HasAnyChild(self):
        return self.HasLeftChild or self.HasRightChild

    @property
    def IsChild(self):
        return self.Parent is not None

    @property
    def IsLeftChild(self):
        if not self.IsChild:
            return False
        return self.Parent.LeftChild == self

    @property
    def IsRightChild(self):
        if not self.IsChild:
            return False
        return self.Parent.RightChild == self

    def __repr__(self):
        return f"(Node UID: {id(self)}. Key: {self.NodeKey}. Value: {self.NodeValue})"

    def __str__(self):
        return self.__repr__()


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node: BSTNode = None  # None если в дереве вообще нету узлов
        self.NodeHasKey: bool = False  # True если узел найден
        self.ToLeft: bool = False  # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None
        self.Amount = 0

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        result = self._FindNodeByKey(self.Root, key)
        return result

    def _FindNodeByKey(self, CurrentNode: BSTNode, key):
        if CurrentNode.NodeKey == key:
            result = BSTFind()
            result.Node = CurrentNode
            result.NodeHasKey = True
            return result

        if CurrentNode.NodeKey > key:
            if not CurrentNode.HasLeftChild:
                result = BSTFind()
                result.Node = CurrentNode
                result.ToLeft = True
                return result
            NextCurrentNode = CurrentNode.LeftChild
        else:
            if not CurrentNode.HasRightChild:
                result = BSTFind()
                result.Node = CurrentNode
                result.ToLeft = False
                return result
            NextCurrentNode = CurrentNode.RightChild

        return self._FindNodeByKey(NextCurrentNode, key)

    def AddKeyValue(self, key, val):
        SearchResult = self._FindNodeByKey(self.Root, key)
        if SearchResult.NodeHasKey:
            return False
        ParentNode = SearchResult.Node
        NewNode = BSTNode(key, val, ParentNode)
        if SearchResult.ToLeft:
            ParentNode.LeftChild = NewNode
        else:
            ParentNode.RightChild = NewNode
        self.Amount += 1
        return True

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return self._FinMinMax(FromNode, FindMax)

    def _FinMinMax(self, FromNode, FindMax):
        ChildNode = FromNode.RightChild if FindMax else FromNode.LeftChild
        if ChildNode is None:
            return FromNode
        return self._FinMinMax(ChildNode, FindMax)

    def _FindSuccessorNode(self, Node: BSTNode):
        if not Node.HasAnyChild:
            return Node
        if not Node.HasLeftChild and Node.HasRightChild:
            return Node
        if Node.HasLeftChild:
            return self._FindSuccessorNode(Node.LeftChild)

    def DeleteNodeByKey(self, key):
        Result = self._FindNodeByKey(self.Root, key)
        if not Result.NodeHasKey:
            return False

        NodeToDelete = Result.Node

        if not NodeToDelete.HasAnyChild:
            self._RemoveNodeFromParent(NodeToDelete)
        elif NodeToDelete.HasBothChildren:
            SuccessorNode = self._FindSuccessorNode(NodeToDelete.RightChild)
            self._UnbindChildFromParent(SuccessorNode)

            if not SuccessorNode.HasLeftChild and SuccessorNode.HasRightChild:
                self._BindChildToParent(NodeToDelete.RightChild, SuccessorNode.RightChild, ToLeft=True)

            self._BindChildToParent(SuccessorNode, NodeToDelete.LeftChild, NodeToDelete.LeftChild.IsLeftChild)
            self._BindChildToParent(SuccessorNode, NodeToDelete.RightChild, NodeToDelete.RightChild.IsLeftChild)

            self._BindChildToParent(NodeToDelete.Parent, SuccessorNode, NodeToDelete.IsLeftChild)
        elif NodeToDelete.HasLeftChild:
            self._BindChildToParent(NodeToDelete.Parent, NodeToDelete.LeftChild, Result.ToLeft)
        elif NodeToDelete.HasRightChild:
            self._BindChildToParent(NodeToDelete.Parent, NodeToDelete.RightChild, Result.ToLeft)

    def _UnbindChildFromParent(self, UnbindingChild: BSTNode):
        Parent = UnbindingChild.Parent
        if Parent is None:
            return False
        if Parent.LeftChild == UnbindingChild:
            Parent.LeftChild = None
        elif Parent.RightChild == UnbindingChild:
            Parent.RightChild = None
        else:
            return False
        return True


    def _BindChildToParent(self, Parent: BSTNode, NewChild: BSTNode, ToLeft: bool):
        if Parent is None:
            return
        if ToLeft:
            Parent.LeftChild = NewChild
        else:
            Parent.RightChild = NewChild
        NewChild.Parent = Parent

    def _RemoveNodeFromParent(self, Node: BSTNode):
        ParentNode = Node.Parent
        if ParentNode is None:
            return False
        if Node == ParentNode.LeftChild:
            ParentNode.LeftChild = None
        elif Node == ParentNode.RightChild:
            ParentNode.RightChild = None
        return True

    def Count(self):
        if self.Root is None:
            return 0
        return self._Count(self.Root)

    def _Count(self, Node: BSTNode):
        if not Node.HasAnyChild:
            return 1
        if Node is None:
            return 0
        Counter = 1
        return Counter + self._Count(Node.LeftChild) + self._Count(Node.RightChild)
