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

        curr_node = head
        node_list = []
        while curr_node:
            node_list.append(curr_node)
            curr_node = curr_node.next

        total_nodes = len(node_list)
        if total_nodes % 2 != 0:
            half_index = total_nodes / 2 + 1
        else:
            half_index = total_nodes / 2

        new_node_list = [0] * total_nodes
        magic = 0
        for i in range(total_nodes):
            if i + 1 < half_index:
                new_node_list[i + magic] = node_list[i]
                magic += 1
            elif i + 1 == half_index:
                new_node_list[i + magic] = node_list[i]
                if total_nodes % 2 == 0:
                    magic += 1
            else:
                new_node_list[len(node_list) - (i + 1) + magic] = node_list[i]
                magic -= 1

        for i in range(total_nodes - 1):
            new_node_list[i].next = new_node_list[i + 1]

        new_node_list[total_nodes - 1].next = None
