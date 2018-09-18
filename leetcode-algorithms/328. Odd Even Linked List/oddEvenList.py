# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddTail = head
        if head.next:
            evenHead = head.next
            evenTail = head.next
        else:
            return head
        while evenTail:
            if evenTail.next:
                temp = evenTail.next.next
                evenTail.next.next = evenHead
                oddTail.next = evenTail.next
                evenTail.next = temp

                evenTail = evenTail.next
                oddTail = oddTail.next
            else:
                return head
        return head

solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
result = solution.oddEvenList(l1)
print(solution.sum)