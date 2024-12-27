# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        from collections import deque, defaultdict

        itr = root
        levels = 0
        q = deque([itr])
        level = list()
        while q:

            n = len(q)
            print("n = ", n)
            reverse = True if n % 2 == 1 else False
            for _ in range(n):
                node = q.popleft()
                print(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if levels % 2 == 1:
                values = [node.val for node in level][::-1]
                for i, node in enumerate(level):
                    node.val = values[i]

            levels += 1
        print(levels)
        return root


