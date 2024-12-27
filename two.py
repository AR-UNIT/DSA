def resultsArray(nums, k):
    def checkSorted(window):
        print(window)
        n = len(window)
        if n == 1:
            return True
        prev = window[0]
        for i in range(1, n):
            current = window[i]
            print(prev, current)
            if not (prev + 1 == current):
                return False
            prev = current
        return True

    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    n = len(nums)
    res = []

    for i in range(0, n):
        window = nums[i:i + k]
        if (len(window) == k):
            if not checkSorted(nums[i:i + k]):
                res.append(-1)
            else:
                res.append(window[-1])

    return res


array = [1, 2, 3, 4, 3, 2, 5]
k = 3
# array = [2,2,2,2,2]
# k = 4
# array = [3,2,3,2,3,2]
# k = 2
# array = [1, 3, 4]
# k = 2
print(resultsArray(array, k))
