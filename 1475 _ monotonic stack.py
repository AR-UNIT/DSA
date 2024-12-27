class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """

        res = prices[::]  # Create a copy of prices to store the results
        stack = list() # Monotonic stack to store indices


        # storing the index of elems in list in stack so that:
        #   1. we can update the result list in place, even for any duplicate elements, without any extra steps
        #   2.


        '''
        while traversing through the stack, we want to check do 2 things using a decreasing monotonic stack:
            1. if the current elem in for loop is lesser than the top elem at the stack, 
                then we have found the next lesser element to subtract from element at top of stack,

            2. if the current elem in for loop is greater than top of stack, then we need to add it to stack,
                so that anything that comes next and is lesser could pop it, and update the value in res

            THIS WHOLE CONCEPT WORKS BECAUSE 
                (I) we are traversing from left to right while building the stack
                (II) we add elements at end top of stack / right end of the list
                (III) as soon as we see an element that is lesser than top of stack, we have found the
                        next smallest element for that top of stack
        '''
        for i, val in enumerate(prices):
            # Check if current price is smaller or equal to the price at the top of the stack
            while stack and prices[stack[-1]] >= val:
                idx = stack.pop()  # Pop the index from the stack
                res[idx] -= val  # Apply the discount
            stack.append(i)  # Push the current index onto the stack

        return res