# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        p = None
        root = TreeNode(preorder[0])
        del preorder[0]
        stack = [root]

        while True:
            if inorder[0] == stack[-1].val:
                p = stack.pop()
                del inorder[0]
                if not inorder:
                    break
                if stack and inorder[0] == stack[-1].val:
                    continue
                p.right = TreeNode(preorder[0])
                del preorder[0]
                stack.append(p.right)
            else:
                p = TreeNode(preorder[0])
                del preorder[0]
                stack[-1].left = p
                stack.append(p)
        return root

    def buildTree_self(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        del preorder[0]
        stack = [root]

        while True:
            if inorder[0] == stack[-1].val:
                p = stack.pop()
                del inorder[0]
                if not inorder:
                    break
                if stack and inorder[0] == stack[-1].val:
                    continue
                p.right = TreeNode(preorder[0])
                del preorder[0]
                stack.append(p.right)
            else:
                p = TreeNode(preorder[0])
                del preorder[0]
                stack[-1].left = p
                stack.append(p)
        return root
