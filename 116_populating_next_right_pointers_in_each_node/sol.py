# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            pre = root
            cur = None
            while pre.left:
                cur = pre
                while cur:
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                    cur = cur.next
                pre = pre.left

    def connect_self(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return

        first_node_at_this_level = root
        while first_node_at_this_level.left:  # means there is next level
            p = first_node_at_this_level
            while p:
                p.left.next = p.right
                if p.next:
                    p.right.next = p.next.left
                p = p.next
            first_node_at_this_level = first_node_at_this_level.left
