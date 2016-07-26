# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        if not root:
            return 0
        stackOfNode = [root]
        stackOfString = [root.val]
        while stackOfNode:
            currNode = stackOfNode.pop()
            currString = stackOfString.pop()
            if currNode.left:
                stackOfNode.append(currNode.left)
                stackOfString.append(currString * 10 + currNode.left.val)
            if currNode.right:
                stackOfNode.append(currNode.right)
                stackOfString.append(currString * 10 + currNode.right.val)
            if not currNode.left and not currNode.right:
                result.append(currString)
        return sum(result)

    def sumNumbers_self(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        node_stack = [root]
        num_stack = [root.val]
        all_nums = []

        while node_stack:
            node = node_stack.pop()
            num = num_stack.pop()
            if not node.left and not node.right:
                all_nums.append(num)

            if node.left:
                node_stack.append(node.left)
                num_stack.append(num * 10 + node.left.val)

            if node.right:
                node_stack.append(node.right)
                num_stack.append(num * 10 + node.right.val)
        return sum(all_nums)
