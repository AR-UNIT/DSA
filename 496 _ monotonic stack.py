class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # stores index of value, decreasing order of value (monotonic)
        stack = list()

        res = [-1] * len(nums2)
        for i, val in enumerate(nums2):
            # if current elem is greater than the TOS val
            # if stack and val > nums2[stack[-1]]:
            # while current elem is greater than TOS val
            while stack and val > nums2[stack[-1]]:
                elem_idx = stack.pop()
                res[elem_idx] = val
            # else:
            stack.append(i)
        print(res)

        # res stores the next greater element for every element in n2,
        # we can use this to create every greater element in n1

        n2_index_map = {val: i for i, val in enumerate(nums2)}
        print(n2_index_map)
        soln = [-1] * len(nums1)
        for i, val in enumerate(nums1):
            soln[i] = res[n2_index_map[val]]

        return soln

'''
what is the algo?
 -> decreasing monotonic stack
    basically, for taking an input array, and creating an array with next greater element for every element:
    -> maintain a decreasing monotonic stack of element indexes while doing o(n) traversal of original array:
        -> when current element in input array is greater than the element at TOS index,
            then we know that the next greater element for the element at TOS is the current element.
            so while TOS index elem is lesser than the current elem in input array:
                -> keep popping TOS, and set the res[TOS index] to current elem    
    
why a decreasing monotonic stack?
    -> the basic idea is that we only want memory for decreasing elements, i.e elements we could not find the
        next greater element for
        -> if we see current_elem is greater, we can immediately assign it as next greater for previous elem
        -> if we see current_elem is lesser, we are storing it in stack, and waiting for an element to come as 
            current_elem, where the current_elem will be greater than the TOS, and will remove all elements from stack,
            which are lesser than current elem  
'''