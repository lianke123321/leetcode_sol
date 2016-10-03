# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            levelNum = len(queue)
            temp = []
            for i in range(levelNum):
                cur = queue[0]
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                del queue[0]
            result.append(temp)
        return list(reversed(result))


class Solution_self(object):
    def recursion(self, root, depth, result):
        if not root:
            return
        if len(result) == depth:
            result.append([])
        result[depth].append(root.val)
        self.recursion(root.left, depth + 1, result)
        self.recursion(root.right, depth + 1, result)

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.recursion(root, 0, result)
        return list(reversed(result))

    def levelOrder_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        q = [root]
        while q:
            length, tmp = len(q), []
            for i in xrange(length):
                curr = q[0]
                tmp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                q.pop(0)
            result.append(tmp)
        return list(reversed(result))
