class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_example_tree():
    # Level 0
    root = TreeNode(3)

    # Level 1
    root.left = TreeNode(5)
    p = root.left
    root.right = TreeNode(1)
    q = root.right

    # Level 2
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # Level 3
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    return root, p, q


def print_tree(node, level=0, side="root"):
    """ Helper function to print the tree structure """
    if node:
        print(" " * (4 * level) + f"{side}: {node.val}")
        print_tree(node.left, level + 1, "L")
        print_tree(node.right, level + 1, "R")





class Solution(object):
    def __init__(self):
        self.path = []


    # think like a tree root at every node, get a working soln first

    # for every root/node:
        # we know that if left/right contains p, and left/right contains q,
        # where both p and q are in either left or right mutually exclusive,
        # then current node must be root, return it upwards

    # if only left or right contains both, we have to go to only left or right, we must return l or r,
    # whichever is non null, this will allow propagating the solution upwards
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return True

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r


tree_root, p, q = build_example_tree()


object = Solution()
object.lowestCommonAncestor(tree_root,p,q)