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
        countA, countB = 0, 0
        headA_dup, headB_dup = headA, headB

        while headA != None and headB != None:
            countA += 1
            countB += 1
            headA = headA.next
            headB = headB.next

        def compare(headB, countA, countB, headA_dup, headB_dup):
            while headB != None:
                countB += 1
                headB = headB.next
            headA, headB = headA_dup, headB_dup
            intersection = countB - countA
            for i in range(intersection):
                headB = headB.next
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA

        if headA == None:
            return compare(headB, countA, countB, headA_dup, headB_dup)
        elif headB == None:
            return compare(headA, countB, countA, headB_dup, headA_dup)




