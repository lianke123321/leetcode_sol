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
        diff, result = abs(root.val - target), root.val
        while p:
            new_diff = abs(p.val - target)
            if new_diff < diff:
                diff, result = new_diff, p.val
                if diff == 0:
                    return result
            p = p.left if target < p.val else p.right
        return result
