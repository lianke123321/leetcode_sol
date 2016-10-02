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
        dummy = ListNode(0)
        dummy.next = head
        front = dummy
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if front.next == cur:
                front = front.next
            else:
                front.next = cur.next
            cur = cur.next
        return dummy.next

    def deleteDuplicates_self(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        front, p = dummy, head
        while p:
            while p.next and p.next.val == p.val:
                p = p.next
            if front.next == p:
                front = front.next
            else:
                front.next = p.next
            p = front.next
        return dummy.next

sol = Solution()
head = ListNode(1)
first_node = ListNode(2)
second_node = ListNode(2)
head.next = first_node
first_node.next = second_node

result = head
while result:
    print result.val
    result = result.next

result = sol.deleteDuplicates_self(head)
print '============'
while result:
    print result.val
    result = result.next
