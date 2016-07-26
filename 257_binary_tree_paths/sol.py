# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result
        stackOfNode = [root]
        stackOfString = [str(root.val)]
        while stackOfNode:
            currNode = stackOfNode.pop()
            currString = stackOfString.pop()
            if currNode.left:
                stackOfNode.append(currNode.left)
                stackOfString.append(currString + '->' + str(currNode.left.val))
            if currNode.right:
                stackOfNode.append(currNode.right)
                stackOfString.append(currString + '->' + str(currNode.right.val))
            if not currNode.left and not currNode.right:
                result.append(currString)
        return result

    def binaryTreePaths_self(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result

        path_stack = [str(root.val)]
        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            path = path_stack.pop()
            if not node.left and not node.right:
                result.append(path)

            if node.left:
                node_stack.append(node.left)
                path_stack.append(path + '->' + str(node.left.val))
            if node.right:
                node_stack.append(node.right)
                path_stack.append(path + '->' + str(node.right.val))
        return result
