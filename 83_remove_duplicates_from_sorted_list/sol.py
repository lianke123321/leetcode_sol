# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                #temp = cur.next
                #cur.next = cur.next.next
                #del temp
                cur.next = cur.next.next
            else:
                cur = cur.next

        '''t = head
        while t:
            print t.val
            t = t.next'''

        return head

    def deleteDuplicates_self(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        while curr_node and curr_node.next:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return head