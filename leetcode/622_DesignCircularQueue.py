# https://leetcode.com/problems/task-scheduler/
# Design queue as double-linked list

class Node:
    def __init__(self, value):
        self.val = value
        self.pre = self.next = None
        
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxsize = k
        self.current_size = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.current_size == 0:
            self.head = self.tail = Node(value)
            self.head.next = self.tail
            self.tail.pre = self.head
        else:
            new_el = Node(value)
            self.tail.next, new_el.pre = new_el, self.tail
            self.tail = new_el
        self.current_size += 1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.current_size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.pre = None
        self.current_size -= 1
        return True
    
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.current_size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.current_size == self.maxsize
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
