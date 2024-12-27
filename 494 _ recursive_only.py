class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        # need to incorporate dp into this
        n = len(nums)
        res = [0]
        # backtrack func to try all the different combinations
        def dfs(i,summ):
            if i > n:
                return
            if i == n:
                if summ == target:
                    res[0] += 1
                return
            # add and dfs
            summ += nums[i]
            dfs(i+1,summ)

            # cleanup + subtract and dfs
            summ -= 2 * nums[i]
            dfs(i+1,summ)

        dfs(0,0)
        return res[0]