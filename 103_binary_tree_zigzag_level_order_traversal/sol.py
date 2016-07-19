# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        queue = [root]
        count = 0
        while queue:
            count += 1
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
            if count % 2 == 0:
                result.append(list(reversed(temp)))
            else:
                result.append(temp)
        return result


class Solution_self(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.recursion(root, 0, result)
        for i in xrange(len(result)):
            if i % 2 == 1:
                result[i] = list(reversed(result[i]))
        return result

    def recursion(self, root, depth, result):
        if not root:
            return
        if len(result) == depth:
            result.append([])
        result[depth].append(root.val)
        self.recursion(root.left, depth + 1, result)
        self.recursion(root.right, depth + 1, result)
