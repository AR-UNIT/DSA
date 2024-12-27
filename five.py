from collections import Counter


def canArrange(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: bool
    """

    arr_sum = sum(arr)
    print(arr_sum)
    if arr_sum % k != 0:
        return False

    n = len(arr)
    max_number_of_pairs = n / 2

    pairs = list()
    number_counts = Counter(arr)
    reset = Counter(arr)

    def dfs(i, j, pairs, ncts):
        # print(i,j)
        print(pairs)
        if i == n or j == n:
            return False

        if len(pairs) == (n / 2):
            return True

        if ncts[arr[i]] == 0 or ncts[arr[j]] == 0:
            return False

        if (arr[i] + arr[j]) % k == 0 and ncts[arr[i]] > 0 and ncts[arr[j]] > 0 and i != j:
            pairs.append((arr[i], arr[j]))
            ncts[arr[i]] -= 1
            ncts[arr[j]] -= 1

        return dfs(i + 1, j, pairs, ncts) or dfs(i, j + 1, pairs, ncts)

    return dfs(0, 0, pairs, number_counts)
    # for i in range(n):
    #     for j in range(n):
    #         if len(pairSet) == max_number_of_pairs:
    #             print(pairSet)
    #             return True
    #
    #         if i == j:
    #             continue
    #
    #         if (arr[i] + arr[j]) % k == 0 and number_counts[arr[i]] > 0 and number_counts[arr[j]] > 0:
    #             pairSet.add((arr[i], arr[j]))
    #             number_counts[arr[i]] -= 1
    #             number_counts[arr[j]] -= 1
    #
    # return False


# arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
# k = 5

arr = [75, 5, -5, 75, -2, -3, 88, 10, 10, 87]
k = 85
print(canArrange(arr, k))
