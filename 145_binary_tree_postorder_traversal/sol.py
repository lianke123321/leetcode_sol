# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        p = root
        LastVisited = None
        while (p != None and p.val != '#') or stack:
            while p != None and p.val != '#':
                stack.append(p)
                p = p.left
            p = stack[-1]
            if (p.right == None or p.right.val == '#') or LastVisited == p.right:
                result.append(p.val)
                LastVisited = p
                stack.pop()
                p = None
            else:
                p = p.right
        return result

    def postorderTraversal_self(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        last_visited = None
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack[-1]
            if p.right is None or last_visited == p.right:
                result.append(p.val)
                last_visited = p
                stack.pop()
                p = None
            else:
                p = p.right

        return result


class Solution_recursive(object):
    def __init__(self):
        self.result = []
        self.stack = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return self.result

        self.stack.append(root)
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.visit(root)
        self.stack.pop()

        if len(self.stack) == 0:
            return self.result

    def visit(self, node):
        self.result.append(node.val)
