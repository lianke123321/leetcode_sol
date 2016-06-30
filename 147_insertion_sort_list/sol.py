# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        p = head
        last = head
        curr = p.next
        while curr:
            # if val is greater than ot equal to last node
            # append curr to sorted list, and move to next
            if curr.val >= last.val:
                last.next = curr
                last = curr
                curr = curr.next
            # if val is less than or equal to first node
            # set this node to be the new head
            elif curr.val <= head.val:
                next = curr.next
                curr.next = head
                head = curr
                p = head
                last.next = next
                curr = last.next
            # if val falls into first and last sorted nodes
            else:
                next = curr.next
                # go through sorted list from start again
                # using p pointer
                while True:
                    if curr.val > p.next.val:
                        p = p.next
                    else:
                        # found the place to insert curr
                        orig_p_next = p.next
                        p.next = curr
                        curr.next = orig_p_next
                        last.next = next
                        curr = last.next
                        p = head
                        break
        return head
