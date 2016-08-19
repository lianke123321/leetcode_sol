# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        p = root
        while (p != None and p.val != '#') or stack:
            while p != None and p.val != '#':
                result.append(p.val)
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                p = p.right
        return result

    def preorderTraversal_self(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        p = root
        while p or stack:
            while p:
                result.append(p.val)
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                p = p.right

        return result

    def preorderTraversal_self_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node:
            result.append(node.val)
            self.helper(node.left, result)
            self.helper(node.right, result)
