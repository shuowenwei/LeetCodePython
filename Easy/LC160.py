# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/intersection-of-two-linked-lists/

labuladong: https://labuladong.gitee.io/algo/1/6/

LC21, LC23, LC141, LC142, LC876, LC160, LC19

LC1650, LC160, LC142
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
        pA, pB = headA, headB 
        while pA != pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next 
            if pB is None:
                pB = headA
            else: 
                pB = pB.next
        return pA 

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
        