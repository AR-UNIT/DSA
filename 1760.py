import heapq


class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        pq = [-x for x in nums]
        for operation in range(maxOperations):
            num = heapq.heappop(pq)
            for i in range(1,nums+1):
                bag_1 = num // 2
                bag_2 = num - bag_1
                heapq.heappush(pq, bag_1)
                heapq.heappush(pq, bag_2)

        print(pq)


nums = [9]
maxOperations = 2
object = Solution()
object.minimumSize(nums, maxOperations)
