# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
            :type inorder: List[int]
            :type postorder: List[int]
            :rtype: TreeNode
            """
        if not inorder:
            return None
        p = None
        root = TreeNode(postorder.pop())
        stack = [root]

        while True:
            if inorder[-1] == stack[-1].val:
                p = stack.pop()
                inorder.pop()
                if not inorder:
                    break
                if stack and inorder[-1] == stack[-1].val:
                    continue
                p.left = TreeNode(postorder.pop())
                stack.append(p.left)
            else:
                p = TreeNode(postorder.pop())
                stack[-1].right = p
                stack.append(p)
        return root

    def buildTree_self(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        stack = [root]

        while True:
            if inorder[-1] == stack[-1].val:
                p = stack.pop()
                inorder.pop()
                if not inorder:
                    break
                if stack and inorder[-1] == stack[-1].val:
                    continue
                p.left = TreeNode(postorder.pop())
                stack.append(p.left)
            else:
                p = TreeNode(postorder.pop())
                stack[-1].right = p
                stack.append(p)
        return root
