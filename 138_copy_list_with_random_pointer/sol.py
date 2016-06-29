# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        next = None
        # first round: make copy of each node,
        # and link them together side-by-side in a single list.
        while p:
            next = p.next
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next = next
            p = next
        # second round: assign random pointers for the copy nodes.
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # third round: restore the original list, and extract the copy list.
        p = head
        pseudoHead = RandomListNode(0)
        copy = None
        copyP = pseudoHead
        while p:
            next = p.next.next
            # extract the copy
            copy = p.next
            copyP.next = copy
            copyP = copy
            # restore the original list
            p.next = next
            p = next

        return pseudoHead.next

    def copyRandomList_self(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        curr = head
        # copy each node and insert each copied node after original
        while curr:
            copy = RandomListNode(curr.label)
            real_next = curr.next
            curr.next = copy
            copy.next = real_next
            curr = real_next

        curr = head
        # assign random value to copied nodes
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        # split previous list into two
        copy_head = None
        while curr:
            if not copy_head:
                copy_head = curr.next
            original = curr
            curr = curr.next.next
            copy = original.next

            # restore true next pointer for original node
            original.next = original.next.next

            if copy.next:
                copy.next = copy.next.next

        return copy_head
