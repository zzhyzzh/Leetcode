class Solution:

    def copyRandomList(self, head):
        if head == None:
            return None
        randomTable = {}
        temp = head
        while temp:
            randomTable[temp] = RandomListNode(temp.label)
            temp = temp.next
        temp = head
        while temp:
            randomTable[temp].next = randomTable.get(temp.next)
            randomTable[temp].random = randomTable.get(temp.random)
            temp = temp.next

        return randomTable.get(head)