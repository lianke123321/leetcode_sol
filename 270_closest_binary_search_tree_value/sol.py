# no Liana solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        p = root
        diff = abs(root.val - target)
        result = root.val
        while p:
            new_diff = abs(p.val - target)
            if new_diff < diff:
                diff = new_diff
                result = p.val
            if target < p.val:
                p = p.left
            else:
                p = p.right
        return result
