# Definition for singly-linked list.
# Given linked list: 1->2->3->4->5, and n = 2.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    depth = 0
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            self.depth = 1
            if n == 1:
                return None
            else:
                return head
        else:
            lst = self.removeNthFromEnd(head.next, n)
            self.depth += 1
            if self.depth == n:
                return lst
            else:
                head.next = lst
                return head


solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
result = solution.removeNthFromEnd(l1, 2)
print(result)
print(type(result))
