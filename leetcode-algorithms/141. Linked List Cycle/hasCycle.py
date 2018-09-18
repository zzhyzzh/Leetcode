class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
            else:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False

solution = Solution()
result = solution.groupAnagrams(
    ["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
print(type(result))