# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
the basic condition is that there should be no nodes without a left child only
either both left and right child missing(leaf) or only right child missing

thus we can optimize count, because no left node will have a left-child missing and right child present
    if left child missing, then no right child as well

    if there is a left child at this level, then thre

'''
class Solution(object):
    def __init__(self):
        self.count = 0

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(root):
            if root == None:
                return
            print(root.val)
            self.count += 1

            self.countNodes(root.left)
            if root.left != None:
                self.countNodes(root.right)
                return

        dfs(root)
        return self.count


