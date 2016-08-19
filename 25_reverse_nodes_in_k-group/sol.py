# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                count -= 1
                temp = head.next
                head.next = cur
                cur = head
                head = temp
            head = cur
        return head

    def reverseKGroup_self(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while curr and count != k:
            curr = curr.next
            count += 1

        # if count < k then do nothing and return
        # original head
        if count == k:
            # now call itself recursively, curr will
            # be the head of the reverse list of new
            # list without first k nodes, directly
            # use curr as 'last' in reverse_linked_list
            # problem
            last = self.reverseKGroup(curr, k)
            while count > 0:
                count -= 1
                next = head.next
                head.next = last
                last = head
                head = next
            head = last
        return head
