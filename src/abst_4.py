class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.tree_size = tree_size
        self.Tree = [None] * tree_size  # массив ключей

    def __len__(self):
        return len(self.Tree)

    def __getitem__(self, NodeIdx):
        return self.Tree[NodeIdx]

    def GetLeftChildIdx(self, CurrentIdx):
        return 2 * CurrentIdx + 1

    def GetRightChildIdx(self, CurrentIdx):
        return 2 * CurrentIdx + 2

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        IndexPointer = 0

        while True:
            if IndexPointer >= len(self):
                return None

            CurrentKey = self.Tree[IndexPointer]

            if CurrentKey is None:
                return -IndexPointer

            if CurrentKey == key:
                return IndexPointer
            elif CurrentKey > key:
                IndexPointer = self.GetLeftChildIdx(IndexPointer)
            elif CurrentKey < key:
                IndexPointer = self.GetRightChildIdx(IndexPointer)

    @property
    def RootNode(self):
        return self.Tree[0]

    def AddKey(self, key):
        Index = self.FindKeyIndex(key)
        if Index is None:
            return -1
        if Index == 0 and len(self) > 0 and self.RootNode is None:
            self.Tree[0] = key
            return 0
        if Index >= 0:
            return Index
        if Index < 0:
            InvertedIndex = -Index
            self.Tree[InvertedIndex] = key
            return InvertedIndex
