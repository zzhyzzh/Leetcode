class MyLinkedList(object):

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        # self.index = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        temp = self.head
        while index != 0 and temp != self.tail:
            temp = temp.next
            index -= 1
        if index != 0 or temp == None:
            return -1
        else:
            return temp.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            self.head = self.ListNode(val)
            self.tail = self.head
        else:
            temp = self.ListNode(val)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.tail == None:
            self.tail = self.ListNode(val)
            self.head = self.tail
        else:
            temp = self.ListNode(val)
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        temp = self.head
        if temp == None:
            if index == 0:
                self.addAtHead(val)
            return
        while temp != self.tail.next and index != 0:
            temp = temp.next
            index -= 1
        if index != 0:
            return
        else:
            if temp == self.tail.next:
                self.addAtTail(val)
                return
            if temp == self.head:
                self.addAtHead(val)
                return
            else:
                insert = self.ListNode(val)
                insert.next = temp
                temp.prev.next = insert
                insert.prev = temp.prev
                temp.prev = insert

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        temp = self.head
        while temp != self.tail and index != 0:
            temp = temp.next
            index -= 1
        if index != 0:
            return
        else:
            if temp == self.head:
                self.head = temp.next
            if temp == self.tail:
                self.tail = temp.prev
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev


linkedList = MyLinkedList()
linkedList.get(0)
linkedList.addAtIndex(1, 2)
linkedList.get(0)
linkedList.get(1)
linkedList.addAtIndex(0, 1)
linkedList.get(0)
linkedList.get(1)
