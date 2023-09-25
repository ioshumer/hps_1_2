class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    @property
    def amount_of_nodes(self):
        """Количество реальных элементов массива"""
        return len(self.HeapArray) - self.HeapArray.count(None)

    @property
    def size(self):
        """Общая длинна массива для хранения узлов"""
        return len(self.HeapArray)

    def __len__(self):
        return self.amount_of_nodes

    def IsIdxInHeap(self, Idx):
        return 0 <= Idx < len(self)

    def GetLeftChildIdx(self, CurrentIdx):
        Result = 2 * CurrentIdx + 1
        return Result if self.IsIdxInHeap(Result) else None

    def GetRightChildIdx(self, CurrentIdx):
        Result = 2 * CurrentIdx + 2
        return Result if self.IsIdxInHeap(Result) else None

    def GetParentIdx(self, CurrentIdx):
        Result = (CurrentIdx + 1) // 2 - 1
        return Result if self.IsIdxInHeap(Result) else None

    @property
    def EmptyIdx(self):
        try:
            return self.HeapArray.index(None)
        except ValueError:
            return None

    @property
    def LastIdx(self):
        return self.amount_of_nodes - 1

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        StorageSize = 2 ** (depth + 1) - 1
        if StorageSize < len(a):
            return None
        self.HeapArray = [None] * StorageSize

        for item in a:
            self.Add(item)

    def GetMax(self):
        if self.amount_of_nodes == 0:
            return -1

        HeapMaxElem = self.HeapArray[0]
        HeapLastIdx = self.LastIdx

        if HeapLastIdx == 0:
            self.HeapArray[0] = None
            return HeapMaxElem

        HeapLastElem = self.HeapArray[HeapLastIdx]
        self.HeapArray[HeapLastIdx] = None
        CurrentIdx = 0
        self.HeapArray[CurrentIdx] = HeapLastElem

        self._PushElemDown(CurrentIdx)
        return HeapMaxElem

    def _GetIdxOfMaxElem(self, FirstIdx, SecondIdx):
        if FirstIdx is None and SecondIdx is None:
            return None
        if FirstIdx is None:
            return SecondIdx
        if SecondIdx is None:
            return FirstIdx
        if self.HeapArray[FirstIdx] > self.HeapArray[SecondIdx]:
            return FirstIdx
        else:
            return SecondIdx

    def _PushElemDown(self, CurrentIdx):
        if CurrentIdx is None:
            return False

        LeftChildIdx = self.GetLeftChildIdx(CurrentIdx)
        RightChildIdx = self.GetRightChildIdx(CurrentIdx)

        MaxChildIdx = self._GetIdxOfMaxElem(LeftChildIdx, RightChildIdx)
        if MaxChildIdx is None:
            return None

        if self.HeapArray[CurrentIdx] > self.HeapArray[MaxChildIdx]:
            return None

        self._SwapNodes(CurrentIdx, MaxChildIdx)
        self._PushElemDown(MaxChildIdx)

    def Add(self, key):
        EmptyIdx = self.EmptyIdx
        if EmptyIdx is None:
            return False
        if EmptyIdx == 0:
            self.HeapArray[0] = key
            return True
        self._Add(key, EmptyIdx)
        return True

    def _SwapNodes(self, FirstIdx, SecondIdx):
        temp = self.HeapArray[FirstIdx]
        self.HeapArray[FirstIdx] = self.HeapArray[SecondIdx]
        self.HeapArray[SecondIdx] = temp

    def _Add(self, key, CurrentIdx):

        ParentIdx = self.GetParentIdx(CurrentIdx)
        if ParentIdx is None:
            return
        ParentKey = self.HeapArray[ParentIdx]

        self.HeapArray[CurrentIdx] = key

        if key < ParentKey:
            return

        self._SwapNodes(ParentIdx, CurrentIdx)
        self._Add(key, ParentIdx)
