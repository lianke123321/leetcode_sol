# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = True
        stack = []
        p = root
        pre = None
        while (p != None and p.val != '#') or stack:
            if p != None and p.val != '#':
                stack.append(p)
                p = p.left
            else:
                temp = stack.pop()
                if (pre != None and pre.val != '#') and temp.val <= pre.val:
                    return False
                pre = temp
                p = temp.right
        return result

    def isValidBST_self(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        p, last = root, None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                if last and p.val <= last.val:
                    return False
                last = p
                p = p.right
        return True

