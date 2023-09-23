class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    @property
    def length(self):
        return len(self.HeapArray) - self.HeapArray.count(None)

    def __len__(self):
        return self.length

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

    def GetSiblingIdx(self, CurrentIdx):
        ParentIdx = self.GetParentIdx(CurrentIdx)
        if ParentIdx is None:
            return None
        ParentLeftChildIdx = self.GetLeftChildIdx(ParentIdx)
        ParentRightChildIdx = self.GetRightChildIdx(ParentIdx)

        return ParentRightChildIdx if ParentRightChildIdx != CurrentIdx else ParentLeftChildIdx

    @property
    def EmptyIdx(self):
        try:
            return self.HeapArray.index(None)
        except ValueError:
            return None

    @property
    def LastIdx(self):
        EmptyIdx = self.EmptyIdx
        return len(self.HeapArray) - 1 if EmptyIdx is None else EmptyIdx - 1

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
        if self.length == 0:
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
        self._PushElemDown(HeapLastElem, CurrentIdx)

        return HeapMaxElem

    def _GetIdxOfMaxElem(self, FirstIdx, SecondIdx):
        if FirstIdx is None:
            return SecondIdx
        if SecondIdx is None:
            return FirstIdx
        MaxElem = max(self.HeapArray[FirstIdx], self.HeapArray[SecondIdx])
        return FirstIdx if self.HeapArray[FirstIdx] == MaxElem else SecondIdx

    def _PushElemDown(self, Elem, CurrentIdx):
        if CurrentIdx is None:
            return False

        LeftChildIdx = self.GetLeftChildIdx(CurrentIdx)
        RightChildIdx = self.GetRightChildIdx(CurrentIdx)

        if LeftChildIdx is None and RightChildIdx is None:
            return False

        LeftChildElem = None if LeftChildIdx is None else self.HeapArray[LeftChildIdx]
        RightChildElem = None if RightChildIdx is None else self.HeapArray[RightChildIdx]

        if LeftChildElem is None and RightChildElem is None:
            return False

        if RightChildElem is None:
            IdxOfMaxElem = LeftChildIdx
            MaxElem = LeftChildElem
        elif LeftChildElem is None:
            IdxOfMaxElem = RightChildIdx
            MaxElem = RightChildElem
        else:
            IdxOfMaxElem = self._GetIdxOfMaxElem(LeftChildIdx, RightChildIdx)
            LeftIsMax = LeftChildIdx == IdxOfMaxElem
            MaxElem = self.HeapArray[LeftChildIdx] if LeftIsMax else self.HeapArray[LeftChildIdx]

        if MaxElem > Elem:
            self._SwapNodes(CurrentIdx, IdxOfMaxElem)
            self.HeapArray[CurrentIdx]
            return True

        result = self._PushElemDown(Elem, LeftChildIdx)
        if not result:
            self._PushElemDown(Elem, RightChildIdx)

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
