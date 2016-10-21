# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = l1
        cur = dummy
        while l2:
            while cur.next and cur.next.val <= l2.val:
                cur = cur.next  # if the current list, l1, has a smaller value, then move cur forward
            l1 = cur.next  # otherwise, switch l1 and l2
            cur.next = l2
            l2 = l1
        return dummy.next

    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0:
            return None
        if length == 1:
            return lists[0]
        if length == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[0: length / 2]), self.mergeKLists(lists[length / 2: length]))


class Solution_recursive:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        num_of_lists = len(lists)
        if num_of_lists == 0:
            return None
        elif num_of_lists == 1:
            return lists[0]
        elif num_of_lists == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            return self.mergeTwoLists(self.mergeKLists(lists[:num_of_lists/2]),
                                      self.mergeKLists(lists[num_of_lists/2:]))

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        # can't recursion since it would exceed max depth in this question
        dummy = ListNode(0)
        curr_node = dummy
        while curr_node and (l1 or l2):
            if l1 and l2:
                if l1.val <= l2.val:
                    curr_node.next = l1
                    l1 = l1.next
                else:
                    curr_node.next = l2
                    l2 = l2.next
            elif l1:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next

        return dummy.next


import heapq


class Solution_heapq(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        heap, p = [], dummy
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        while heap:
            _, next_node = heapq.heappop(heap)
            p.next = next_node
            p = p.next
            if p.next:
                heapq.heappush(heap, (p.next.val, p.next))
            p.next = None
        return dummy.next
