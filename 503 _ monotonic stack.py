class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [-1] * len(nums)

        # using decreasing monotonic stack,
        # need memory of smaller numbers we could not find greater value for
        stack = list()
        curr_max = float("-inf")
        for i, val in enumerate(nums):
            curr_max = max(curr_max, val)
            while stack and val > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)

        print(stack)
        for i, val in enumerate(nums):
            while stack and val > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)

        print(stack)
        return res

'''
Same as 496, but with circular array instead. 
The algo is simple. 
Doing same steps 496 but twice, because:
    (I) since the array is circular, at max 2 iterations of array required to find next greater element
        in the order of the array itself
    (II) since the elems with no next greater element are left on the stack after first iteration
        running the algo again will just use the same stack and process the elems on stack correctly considering 
        circular array

'''