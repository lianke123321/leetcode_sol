# no Liana solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        self.recursion(root, result)
        return result

    def recursion(self, root, result):
        if not root:
            return -1

        h = max(self.recursion(root.left, result),
                self.recursion(root.right, result)) + 1
        if len(result) - 1 < h:
            result.append([])

        result[h].append(root.val)
        return h
