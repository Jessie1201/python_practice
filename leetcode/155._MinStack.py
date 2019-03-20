# https://leetcode.com/problems/min-stack/submissions/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.ordered = []
        

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        self.ordered = self.stack[:]
        self.ordered.sort()

    def pop(self) -> None:
        self.stack.pop(0)
        self.ordered = self.stack[:]
        self.ordered.sort()
        

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        if len(self.ordered) == 0:
            return None
        else:
            return self.ordered[0]

if __name__=="__main__":
    obj = MinStack()
    obj.push(-2)
    # print(obj.ordered)
    obj.push(0)
    obj.push(-3)
    param_4 = obj.getMin()
    obj.pop()
    param_5 = obj.top()
    param_6 = obj.getMin()
    print(param_4,param_5,param_6)
