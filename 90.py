class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        n = len(nums)
        nums.sort()

        def backtrack(start, subset):

            if start == n:
                res.append(subset[:])
                return

            j = start

            # we have to skip ahead past repeated number only after making a recursive call to include the repeated number,
            # this way, we can accurately repeat the number as many times as it is present in the nums list,
            # in the subtree formed from the previous call
            subset.append(nums[j])
            backtrack(j + 1, subset)
            subset.pop()

            while j < n - 1 and nums[j] == nums[j + 1]:
                j += 1

            # having created recursion subtree where the repeated numbers start, now we can skip ahead past all the
            # repeated numbers, to start subtrees that are not going to include previous repeated numbers
            backtrack(j + 1, subset)

        backtrack(0, [])
        return res