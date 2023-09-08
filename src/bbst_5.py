def CheckIfTreeFull(array_len):
    checking_value = array_len + 1
    if checking_value < 2:
        return False
    else:
        return (checking_value & (checking_value - 1)) == 0


def GenerateBBSTArray(a):
    InitialArrayLen = len(a)

    if not CheckIfTreeFull(InitialArrayLen):
        return None

    a.sort()

    SortedArray = [None] * InitialArrayLen
    ElementPosition = 0

    result = _RecursiveProcessing(a, SortedArray, ElementPosition)
    return SortedArray


def _RecursiveProcessing(SortingArray: list, SortedArray: list, ElementPosition: int):
    ArrayLength = len(SortingArray)
    MiddleIndex = ArrayLength // 2

    if MiddleIndex == 0:
        print(SortingArray)
        SortedArray[ElementPosition] = SortingArray[0]
        return

    Vertex = SortingArray[MiddleIndex]
    SortedArray[ElementPosition] = Vertex

    LeftChildPosition = ElementPosition * 2 + 1
    LeftPart = SortingArray[:MiddleIndex]
    _RecursiveProcessing(LeftPart, SortedArray, LeftChildPosition)

    RightChildPosition = LeftChildPosition + 1
    RightPart = SortingArray[MiddleIndex+1:]
    _RecursiveProcessing(RightPart, SortedArray, RightChildPosition)


l1 = [50, 25, 75, 13, 37, 63, 88]


print(GenerateBBSTArray(l1))