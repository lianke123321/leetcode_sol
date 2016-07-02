# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList_self(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head

        dummy_odd = ListNode(0)
        dummy_even = ListNode(0)
        odd_curr = dummy_odd
        even_curr = dummy_even
        curr = head
        while curr and curr.next:
            odd_node = curr
            even_node = curr.next
            next_curr = even_node.next

            odd_curr.next = odd_node
            odd_node.next = None
            odd_curr = odd_node

            even_curr.next = even_node
            even_node.next = None
            even_curr = even_node

            curr = next_curr

        # if there is one odd node left
        if curr:
            odd_curr.next = curr
            curr.next = None
            odd_curr = curr

        # concatenate two lists
        odd_curr.next = dummy_even.next

        return dummy_odd.next
