# no Liana solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict, deque
        cols = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, col = queue.pop()
            if node:
                cols[col].append(node.val)
                queue.appendleft((node.left, col - 1))
                queue.appendleft((node.right, col + 1))
        return [cols[i] for i in sorted(cols)]
