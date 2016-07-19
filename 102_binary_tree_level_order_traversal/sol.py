# my solution is exactly the same


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recursion(self, root, depth, result):
        if not root:
            return
        if len(result) == depth:
            result.append([])
        result[depth].append(root.val)
        self.recursion(root.left, depth + 1, result)
        self.recursion(root.right, depth + 1, result)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.recursion(root, 0, result)
        return result
