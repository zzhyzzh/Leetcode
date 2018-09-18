# Definition for singly-linked list.
# Given linked list: 1->2->3->4->5, and n = 2.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        back = dummy
        ahead = dummy
        for i in range(n):
            ahead = ahead.next
        ahead = ahead.next
        while ahead != None:
            back = back.next
            ahead = ahead.next
        back.next = back.next.next
        return dummy.next


solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
result = solution.removeNthFromEnd(l1, 2)
print(result)
print(type(result))
