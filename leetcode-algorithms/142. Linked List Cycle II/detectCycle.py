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
        nodes = set()
        nodes.add(head)
        slow = head
        while slow != None:
            slow = slow.next
            if slow == None or slow in nodes:
                return slow
            else:
                nodes.add(slow)
        return None

solution = Solution()
result = solution.groupAnagrams(
    ["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
print(type(result))