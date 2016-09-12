# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        answer = []
        stack = [[root, answer]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in (None, p, q):
                parent += node,
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                if all(subs):
                    parent += [node]
                else:
                    parent += [max(subs)]
        return answer[0]

    def lowestCommonAncestor_self(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
