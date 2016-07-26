# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        stackOfNode = [root]
        stackOfString = [[root.val]]
        while stackOfNode:
            currNode = stackOfNode.pop()
            currString = stackOfString.pop()
            if currNode.left:
                stackOfNode.append(currNode.left)
                stackOfString.append(currString + [currNode.left.val])
            if currNode.right:
                stackOfNode.append(currNode.right)
                stackOfString.append(currString + [currNode.right.val])
            if not currNode.left and not currNode.right and sum(currString) == total:
                result.append(currString)
        return result

    def pathSum_self(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        node_stack = [root]
        path_stack = [[root.val]]
        while node_stack:
            p = node_stack.pop()
            tmp = path_stack.pop()
            if p.val == sum and not p.left and not p.right:
                result.append(tmp)
            if p.left:
                path_stack.append(tmp + [p.left.val])
                node_stack.append(p.left)
                p.left.val += p.val
            if p.right:
                path_stack.append(tmp + [p.right.val])
                node_stack.append(p.right)
                p.right.val += p.val
        return result
