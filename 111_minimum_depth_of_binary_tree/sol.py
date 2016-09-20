# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left, right) + 1

    def minDepth_self(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        min_left = self.minDepth_self(root.left)
        min_right = self.minDepth_self(root.right)
        if min_left == 0 or min_right == 0:
            return min_left + min_right + 1
        else:
            return min(min_left, min_right) + 1

    def minDepth_iterative(self, root):
        if not root:
            return 0
        q, lvl = [root], 0
        while True:
            lvl += 1
            sz = len(q)
            for i in xrange(sz):
                node = q.pop(0)
                if not node.left and not node.right:
                    return lvl
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
