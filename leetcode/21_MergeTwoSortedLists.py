# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists  
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l2 and l1:
            if l2.val < l1.val:
                return self.mergeTwoLists(l2, l1)

            # l2-list at end of l1-list
            elif l2.val >= l1.val and l1.next == None:
                l1.next = l2
                return l1

            # insert l2-node into l1-link
            elif l2.val >= l1.val and l2.val <= l1.next.val:
                next_insert = l2.next
                l1.next, l2.next = l2, l1.next
                l1.next = self.mergeTwoLists(l1.next, next_insert)
                return l1

            # move to next l1-node
            elif l2.val > l1.next.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            
        return l1 or l2

# better solution from discussion
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b