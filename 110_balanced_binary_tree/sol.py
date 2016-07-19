# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution_self(object):
    def __init__(self):
        self.result = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.result

    def depth(self, root):
        if not root:
            return 0
        else:
            left_depth, right_depth = self.depth(root.left), self.depth(root.right)
            if abs(left_depth - right_depth) > 1:
                self.result = False
            return max(left_depth, right_depth) + 1
