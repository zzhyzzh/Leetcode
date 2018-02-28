# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.list2num(l1)
        num2 = self.list2num(l2)
        self.sum = num1 + num2
        num = str(self.sum)
        l = ListNode(int(num[0]))
        for i in range(1, len(num)):
            li = ListNode(int(num[i]))
            li.next = l
            l = li
        return l

    def list2num(self, l):
        num = l.val
        i = 1
        while l.next is not None:
            l = l.next
            num = num + l.val * (10 ** i)
            i += 1

        return num


solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = solution.addTwoNumbers(l1, l2)
print(solution.sum)
