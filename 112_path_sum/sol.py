# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        stack = []
        p = root
        LastVisited = None
        s = 0
        while (p != None and p.val != '#') or stack:
            while p != None:
                stack.append(p)
                s += p.val
                p = p.left
            p = stack[-1]
            if p.left == None and p.right == None and s == sum:
                return True
            if p.right == None or LastVisited == p.right:
                LastVisited = p
                stack.pop()
                s -= p.val
                p = None
            else:
                p = p.right
        return False

    def hasPathSum_self(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [root]
        while stack:
            p = stack.pop()
            if p.val == sum and not p.left and not p.right:
                return True
            if p.left:
                p.left.val += p.val
                stack.append(p.left)
            if p.right:
                p.right.val += p.val
                stack.append(p.right)
        return False
