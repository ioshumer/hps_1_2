class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    @property
    def length(self):
        return len(self.HeapArray)

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

    def CalcDepth(self, depth):
        return 2**(depth + 1) - 1

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        self.HeapArray = [None] * self.CalcDepth(depth)

        for item in a:
            self.Add(item)

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        return -1  # если куча пуста

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        EmptyIdx = self.EmptyIdx
        if EmptyIdx is None:
            return False
        if EmptyIdx == 0:
            self.HeapArray[0] = key
            return
        self._Add(key, EmptyIdx)

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
