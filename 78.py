class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        subsets = list()

        def dfs(i, subset):
            if i == n:
                subsets.append(subset)
                return

            # not including element

            dfs(i + 1, subset)

            # including element

            subset.append(nums[i])
            dfs(i + 1, subset[:])  # passes copy by value when we do subset[:]

            '''
            cleanup required, because when we recurse back to the caller, then we want to clean up subset object,
            before continuing process in the caller.
            
            IMPORTANT POINT -> Each recursive call works on the same subset object.
            If you modify subset in one recursive call (e.g., subset.append(nums[i])), 
            those changes persist when you return to the caller, unless you explicitly undo them (via subset.pop()).
            
            LIST PASSED IN ARGUMENT IS A SHARED MUTABLE OBJECT.
            
            '''
            subset.pop()

        dfs(0, [])
        return subsets


nums = [1, 2, 3]
object = Solution()
print(object.subsets(nums))
