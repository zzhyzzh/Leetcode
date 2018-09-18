# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA = headA
        tempB = headB
        countA, countB = 0, 0
        while tempA:
            tempA = tempA.next
            countA += 1
        while tempB:
            tempB = tempB.next
            countB += 1
        if countB < countA:
            headA, headB = headB, headA
            countA, countB = countB, countA
        tempA = headA
        tempB = headB
        for i in range(countB - countA):
            tempB = tempB.next
        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next
        return tempA



