# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/intersection-of-two-linked-lists/

"""

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
        pA, pB = headA, headB
        stackA, stackB = 0, 0
        while stackA <= 1 and stackB <= 1:
            if pA == pB:
                return pA
            if pA.next is None and pB.next is None:
                pA = headB
                pB = headA
                stackA += 1 
                stackB += 1
            elif pA.next is None and pB.next is not None:
                pA = headB
                pB = pB.next
                stackA += 1 
            elif pA.next is not None and pB.next is None:
                pB = headA
                pA = pA.next
                stackB += 1
            elif pA.next is not None and pB.next is not None:
                pA = pA.next
                pB = pB.next

        if pA is not None and pA == pB:
            return pA
        else:
            return None

        """
        if not headA or not headB:
            return None
        # make B a circle 
        t2 = headB
        while t2.next:
            t2 = t2.next
        t2.next = headB
        
        #traverse A to enter B circle to find intersection Node 
        dummy = ListNode(-1)
        dummy.next = headA
        fast = dummy
        slow = dummy
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True # B is circle and intersection exists 
                break
            
        if not flag:
            t2.next = None  # not changes B's structure 
            return None
        
        # fast pointer is exactly two times faster than slow pointer 
        tmp = dummy
        while tmp != slow:
            tmp = tmp.next
            slow = slow.next
        
        t2.next = None  # not changes B's structure 
        return tmp
        """
        