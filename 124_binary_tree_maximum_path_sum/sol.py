# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recursion(self, root, maxPath, result):
        if not root:
            return 0
        left = max(0, self.recursion(root.left, maxPath, result))
        right = max(0, self.recursion(root.right, maxPath, result))
        #maxPath = max(maxPath, left + right + root.val)
        result.append(left + right + root.val)
        return root.val + max(left, right)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        maxPath = -2147483648
        self.recursion(root, maxPath, result)
        return max(result)


class Solution_self(object):
    def __init__(self):
        self.result = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.recursion(root)
        return self.result

    def recursion(self, root):
        if not root:
            return 0
        left = max(0, self.recursion(root.left))
        right = max(0, self.recursion(root.right))
        self.result = max(self.result, left + right + root.val)
        return root.val + max(left, right)
