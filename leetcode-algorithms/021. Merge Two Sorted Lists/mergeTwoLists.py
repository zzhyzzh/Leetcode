# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val < l2.val:
            l = ListNode(l1.val)
            l.next = self.mergeTwoLists(l1.next, l2)
        elif l1.val >= l2.val:
            l = ListNode(l2.val)
            l.next = self.mergeTwoLists(l1, l2.next)
        return l
solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
result = solution.mergeTwoLists(l1, l2)
print(result)
print(type(result))
