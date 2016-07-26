# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def height(self, root):
        if not root:
            return -1
        else:
            return 1 + self.height(root.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.height(root)
        if h < 0:
            return 0
        elif self.height(root.right) == h - 1:
            return (1 << h) + self.countNodes(root.right)
        else:
            return (1 << h - 1) + self.countNodes(root.left)


class Solution_self(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        h = self.height(root)
        if self.height(root.right) == h - 1:
            # in this case, left subtree is a full tree
            return (1 << h) + self.countNodes(root.right)
        else:
            return (1 << h - 1) + self.countNodes(root.left)

    def height(self, root):
        if not root:
            return -1
        else:
            return self.height(root.left) + 1
