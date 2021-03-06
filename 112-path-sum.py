# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        if root.left is None and root.right is None:
            return root.val == sum

        remain = sum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)

