# Definition for singly-linked list.
import sys
sys.setrecursionlimit(1000000)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        elif len(lists) >= 3:
            lists_merge = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    lists_merge.append(self.mergeTwoLists(lists[i], lists[i + 1]))
                else:
                    lists_merge.append(lists[i])
            return self.mergeKLists(lists_merge)

    def mergeTwoLists(self, l1, l2):
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
l2 = ListNode(0)
# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)
result = solution.mergeKLists(l1)
print(result)
print(type(result))
