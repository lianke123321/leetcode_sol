# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    def reverseList(self, head):
        last = None
        cur = head  # currentNode
        while cur:
            temp = cur.next  # nextNode
            cur.next = last
            last = cur
            cur = temp
        return last

    def mergeList(self, a, b):
        tail = a
        head = a
        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
        return head

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        a, b = self.splitList(head)
        b = self.reverseList(b)
        head = self.mergeList(a, b)

    def reorderList_self(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

            # split list into 2
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        a, b = head, middle

        # reverse second list
        last = None
        curr = b
        while curr:
            tmp = curr.next
            curr.next = last
            last = curr
            curr = tmp
        b = last

        # combine two lists
        head = a
        tail = a
        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
