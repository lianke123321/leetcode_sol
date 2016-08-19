# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        p = root
        while (p != None and p.val != '#') or stack:
            while p != None and p.val != '#':
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result

    def inorderTraversal_self(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result


    def inorderTraversal_self_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node:
            self.helper(node.left, result)
            result.append(node.val)
            self.helper(node.right, result)
