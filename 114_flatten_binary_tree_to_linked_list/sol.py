# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        result = []
        stack = []
        p = root
        if p:
            stack.append(p)
        while stack:
            p = stack[0]
            result.append(p)
            del stack[0]
            if p.right and p.right.val != '#':
                stack.insert(0, p.right)
            if p.left and p.left.val != '#':
                stack.insert(0, p.left)
        if result:
            p = root
            for i in range(1, len(result)):
                p.left = None
                p.right = result[i]
                p = p.right
