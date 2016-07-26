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
        head = None # head of the next level
        pre = None # the leading node on the next level
        curr = root # current node of current level
        while curr:
            while curr: # iterate on the current level
            # left child
                if curr.left:
                    if pre:
                        pre.next = curr.left
                    else:
                        head = curr.left
                    pre = curr.left
            # right child
                if curr.right:
                    if pre:
                        pre.next = curr.right
                    else:
                        head = curr.right
                    pre = curr.right
            # move to the next node
                curr = curr.next
            # move to the next level
            curr = head
            head = None
            pre = None

    def connect_self(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return

        first_node = root
        while first_node:
            p = first_node
            next_right_most = None
            next_first = None
            while p:
                if p.left and p.right:
                    p.left.next = p.right
                    if next_right_most:
                        next_right_most.next = p.left
                    if not next_first:
                        next_first = p.left
                    next_right_most = p.right
                elif p.left:
                    if next_right_most:
                        next_right_most.next = p.left
                    if not next_first:
                        next_first = p.left
                    next_right_most = p.left
                elif p.right:
                    if next_right_most:
                        next_right_most.next = p.right
                    if not next_first:
                        next_first = p.right
                    next_right_most = p.right
                p = p.next
            first_node = next_first
