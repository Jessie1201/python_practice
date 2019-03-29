# https://leetcode.com/problems/design-linked-list/
# Design your implementation of the linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            return self.head.val
        target = self.head
        for _ in range(1, index+1):
            target = target.next
        return target.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next, self.head = self.head, node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.size == 1:
            self.head.next = node
        else:
            last = self.head
            for _ in range(1, self.size):
                last = last.next
            last.next = node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            pass
        elif index == 0:
            node = Node(val)
            self.head, node.next = node, self.head
            self.size += 1
        elif index == 1:
            node = Node(val)
            self.head.next, self.head.next.next = node, self.head.next
            self.size += 1
        elif 1 < index < self.size:
            pre = self.head
            for _ in range(1, index):
                pre = pre.next
            node = Node(val)
            pre.next, pre.next.next = node, pre.next
            self.size += 1
        elif index == self.size:
            self.addAtTail(val)

        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0<= index < self.size:
            pre = self.head
            for _ in range(1, index):
                pre = pre.next
            pre.next = pre.next.next
            self.size -= 1
        


if __name__=="__main__":
    obj = MyLinkedList()
    # obj.addAtHead(0)
    # obj.addAtTail(3)
    obj.addAtIndex(1,2)
    obj.addAtIndex(0,1)
    # obj.addAtTail(7)
    # obj.addAtHead(1)
    # obj.deleteAtIndex(1)
    print(obj.get(0))
