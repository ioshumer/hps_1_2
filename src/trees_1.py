class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def __repr__(self):
        return f"Node UID: {id(self)}. Value: {self.NodeValue}"

    def __str__(self):
        return self.__repr__()


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
        result = self._TraverseTheTree(self.Root)
        return [result]

    def _TraverseTheTree(self, Node: SimpleTreeNode):
        ChildNodes = Node.Children

        if len(ChildNodes) == 0:
            return None

        NodesList = []

        for ChildNode in ChildNodes:
            Result = self._TraverseTheTree(ChildNode)
            if Result is None:
                StoringValue = {ChildNode: []}
                NodesList.append(StoringValue)
            else:
                NodesList.append(Result)

        return {Node: NodesList}

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
        ChildNodes = Node.Children
        if len(ChildNodes) == 0 and Node is not self.Root:
            return 0

        accumulator = 1

        for ChildNode in ChildNodes:
            accumulator += self._Count(ChildNode)

        return accumulator

    def LeafCount(self):
        # количество листьев в дереве
        return self._LeafCount(self.Root)

    def _LeafCount(self, Node: SimpleTreeNode):
        ChildNodes = Node.Children

        if len(ChildNodes) == 0 and Node is not self.Root:
            return 1

        accumulator = 0

        for ChildNode in ChildNodes:
            accumulator += self._LeafCount(ChildNode)

        return accumulator
