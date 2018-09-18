# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        if ptr == None:
            return head
        while ptr.next != None:
            temp = ptr.next.next
            ptr.next.next = head
            head = ptr.next
            ptr.next = temp
        return head
