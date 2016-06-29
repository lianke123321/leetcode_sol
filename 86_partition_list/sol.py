# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        big = start
        p = start
        while p.next:
            #print 'p = %s, big = %s' % (p.val, big.val)
            if p.next.val >= x:
                p = p.next
            elif p == big:
                big = big.next
                p = p.next
            else:
                temp1 = p.next.next
                temp2 = big.next
                big.next = p.next
                p.next.next = temp2
                p.next = temp1
                big = big.next

        '''t = start
        while t:
            print t.val
            t = t.next'''
        return start.next

    def partition_self(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_dummy_head = ListNode(0)
        small_dummy = small_dummy_head
        big_dummy_head = ListNode(0)
        big_dummy = big_dummy_head
        curr = head
        while curr:
            if curr.val < x:
                small_dummy.next = curr
                small_dummy = curr
            else:
                big_dummy.next = curr
                big_dummy = curr
            curr = curr.next

        big_dummy.next = None
        small_dummy.next = big_dummy_head.next
        return small_dummy_head.next

sol = Solution()
node1 = ListNode(2)
node2 = ListNode(1)
node1.next = node2
node = sol.partition_self(node1, 1.5)
print node.val, node.next.val
