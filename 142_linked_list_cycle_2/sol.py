# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slower = head
        faster = head
        while True:
            if faster == None or faster.next == None:
                return None
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                break
        slower = head
        while True:
            if slower == faster:
                return slower
            else:
                slower = slower.next
                faster = faster.next

    def detectCycle_self(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = head
        while True:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
