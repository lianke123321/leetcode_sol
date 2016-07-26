# no Liana solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.dfs(root.left, 1, root.val),
                   self.dfs(root.right, 1, root.val))

    def dfs(self, node, count, parent_val):
        if not node:
            return count

        count = count + 1 if node.val - parent_val == 1 else 1
        return max(self.dfs(node.left, count, node.val),
                   self.dfs(node.right, count, node.val), count)
