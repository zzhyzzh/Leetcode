# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
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
        l = ListNode(int(num[-1]))
        for i in range(len(num) - 2, -1, -1):
            li = ListNode(int(num[i]))
            li.next = l
            l = li
        return l

    def list2num(self, l):
        num = l.val
        i = 1
        while l.next:
            l = l.next
            num = num * 10 + l.val
            i += 1

        return num