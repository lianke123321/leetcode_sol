# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = head
        while curr:
            if curr.val == val:
                temp = curr.next
                pre.next = temp
                curr.next = None
                curr = temp
            else:
                pre = pre.next
                curr = curr.next
        return dummy.next

    def removeElements_self(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val != val:
                curr = curr.next
            else:
                curr.next = curr.next.next
        return dummy.next

sol = Solution()
head = ListNode(1)
print sol.removeElements_self(head, 1)
