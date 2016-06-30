# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head
        return temp

    def swapPairs_self(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr and curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            next_curr = node2.next
            curr.next = node2
            node2.next = node1
            node1.next = next_curr
            curr = curr.next.next
        return dummy.next
