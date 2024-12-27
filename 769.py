class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        '''
        key observation, 
        the minimum value in a chunk/segment has to be greater than 
        the maximum value of the previous segment
        '''

        chunks = int()
        cur_max = -1
        for i, val in enumerate(arr):

            # if the max number encountered until now is equal to the i,
            # i.e. the max number possible upto this index,
            # then we can increment chunk,
            # because we can break the next coming section and still concatenate afterward and get correct output

            cur_max = max(cur_max, val)
            if cur_max == i:
                chunks += 1

        return chunks

'''
What is the algo?



Why does it work?
'''