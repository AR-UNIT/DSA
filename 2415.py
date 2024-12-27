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
        from collections import deque

        levels = 0
        q = deque([root])
        while q:
            level = list()
            n = len(q)

            # getting the length of the q before we start popping nodes,
            # so that we can identify which level we are processing

            for _ in range(n):
                node = q.popleft()
                level.append(node)
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


'''
what is the algo?
 -> just basic level order traversal
 -> on every odd level, once we have all the nodes of the level in the levels list
    -> get a reversed list of values 
    -> iterate through levels list, and update values accoring to reversed list of values
    
why does the reversal work when we update in for loop?
 -> the nodes maintained at the level list and in q are references to tree nodes 
    -> reference(pointer without memory management) to the object
    -> thus, when we traverse in the tree, we can directly change the variables in the TreeNode.


'''