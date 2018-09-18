# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
            else:
                return None
            slow = slow.next
            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None

solution = Solution()
result = solution.groupAnagrams(
    ["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
print(type(result))