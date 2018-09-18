# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def nodeVal(l):
            if l == None:
                return 0
            else:
                return l.val

        head = None
        carry = 0
        while l1 or l2 or carry:
            preHead = head
            head = ListNode(0)
            digitSum = carry + nodeVal(l1) + nodeVal(l2)
            if digitSum < 10:
                carry = 0
                head.val = digitSum
                head.next = preHead
            elif digitSum >= 10:
                carry = 1
                head.val = digitSum - 10
                head.next = preHead
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        node = None
        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        return node


solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = solution.addTwoNumbers(l1, l2)
print(solution.sum)