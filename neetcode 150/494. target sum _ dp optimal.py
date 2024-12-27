class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # need to incorporate dp into this
        '''
        dp strategy:
            soln case = cur_sum = target_sum and i == n

            What do we want in res?
                -> the number of ways to reach soln case starting at i = 0

            What do we store?
                -> the number of ways to reach soln case from each (i,sum) pair/state 
                -> mapping of (i,sum) -> count

            How is dp saving work?
                -> trimming the decision tree by avoiding repeated work
                -> if we have reach a i,sum state that is already mapped in dp, 
                    the number of ways to reach soln case from that state is already calculated,
                    return early, no need to recalculate 

            How do we get res from dp?
                -> at the end of computation, res is the dp mapping of (0,0) -> count,
                i.e. the number of ways to reach soln state from index 0, and cur_sum = 0
        '''

        # Memoization dictionary
        dp = {}
        n = len(nums)

        def dfs(i, current_sum):
            # If i,current_sum combination seen before, trim decision tree
            # subtree from here already calculated, don't recalculate, just return back
            if (i, current_sum) in dp:
                return

            # Base case: if we've reached the end of the array
            if i == len(nums):
                # if soln case, increment global res counter
                dp[(i, current_sum)] = 1 if current_sum == target else 0
                return

            # Explore the two choices: add or subtract nums[i]
            '''
            after trying these two calls, the work until end index case would be done entirely
            we can save the work done at current node, after we have returned back from 
            traversing down the tree 
            '''
            dfs(i + 1, current_sum + nums[i])
            dfs(i + 1, current_sum - nums[i])

            # Cache the result for this state
            '''
            at every i,cur_sum state, we can explore 2 options to get to soln state:
                -> add nums[i] and continue
                -> subtract nums[i] and continue
            thus to get the total number of ways to reach soln case from current state, 
            we have to sum the result of both calls
            '''
            dp[(i, current_sum)] = dp[(i + 1, current_sum + nums[i])] + dp[(i + 1, current_sum - nums[i])]

        dfs(0, 0)
        print(dp)

        '''
        dp is storing the number of ways to get target sum at i == n from current index,
        the solution will be stored in i = 0, cur_sum = 0
        '''
        return dp[(0, 0)]
