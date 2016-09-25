# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, node):
        if not node:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = self.countNodes(root.left)
        if k <= count:
            return self.kthSmallest(root.left, k)
        elif k > count + 1:
            return self.kthSmallest(root.right, k - 1 - count) # 1 is counted as current node
        return root.val


class Solution_self(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        p, stack, i = root, [], 0
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            i += 1
            if i == k:
                return p.val
            p = p.right
