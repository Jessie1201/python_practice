# https://leetcode.com/problems/intersection-of-two-linked-lists/
# find the node at which the intersection of two singly linked lists begins.
# DIFFICULT - 2 pointers tricky, if wanna search from last linked node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            if not pa.next and not pb.next:
                return None
            pa = pa.next if pa.next else headB
            pb = pb.next if pb.next else headA
        return pa
             
