# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slower = head
        faster = head
        while True:
            if faster == None or faster.next == None:
                return False
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True

    def hasCycle_self(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes_set = set()
        if not head or not head.next:
            return False

        curr_node = head
        while curr_node:
            if curr_node not in nodes_set:
                nodes_set.add(curr_node)
                curr_node = curr_node.next
            else:
                return True

        return False