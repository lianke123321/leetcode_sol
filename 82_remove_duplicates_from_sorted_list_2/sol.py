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
        last_node = None
        curr_node = head
        duplicates = set()
        while curr_node:
            if curr_node.val in duplicates:
                if last_node:
                    last_node.next = curr_node.next
                    curr_node = last_node.next
                else:
                    head = curr_node.next
                    curr_node = head
            elif curr_node.next and curr_node.val == curr_node.next.val:
                if curr_node.val not in duplicates:
                    duplicates.add(curr_node.val)
                if last_node:
                    last_node.next = curr_node.next.next
                    curr_node = last_node.next
                else:
                    head = curr_node.next.next
                    curr_node = head
            else:
                last_node = curr_node
                curr_node = curr_node.next

        return head

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
