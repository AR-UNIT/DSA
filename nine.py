import math
from collections import defaultdict


def toBinary(num):
    binaryMap = defaultdict(int)
    while num > 0:
        power = int(math.log2(num))
        binaryMap[power] = 1
        num = num - 2 ** power
        if num % 2 == 0:
            return convertDictToList(binaryMap)
        if num == 0:
            return convertDictToList(binaryMap)


def convertDictToList(binaryMap):
    lis = [0] * (max(binaryMap.keys()) + 1)
    for i, val in binaryMap.items():
        lis[i] = val
    return lis


def minEnd(n, x):
    """
    :type n: int
    :type x: int
    :rtype: int
    """

    def getNextGreater(lis):
        i = 0
        while i < len(lis) and lis[i] == 1:
            i += 1
        # currently i is either at end of list, or at first index where val 0
        if i < len(lis):
            if lis[i - 1] == 1:
                lis[i] = 1
                while i > 0:
                    i -= 1
                    lis[i] = 0

            else:
                lis[i] = 1
        else:
            lis = [0] * (len(lis))
            lis.append(1)
        return lis

    def checkWholeColumnNotBecoming1(nums, c):
        col = [nums[c] for x in nums]
        print("col:", col)

    lis = toBinary(x)
    nums = [lis[:]]
    while n > 1:
        last = nums[-1]
        current = getNextGreater(last[:])
        nums.append(current)
        n -= 1

    def binaryToDecimal(lis):
        num = 0
        for i, val in enumerate(lis):
            num += val * 2 ** i
        return num

    res = []
    for lis in nums:
        res.append(binaryToDecimal(lis))
        print(lis)
    return res


print(minEnd(3, 1))
print(1 & 2 & 3)
