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
        
        listA = []
        listB = []
        while 1: 
            if headA == None:
                break
            listA.append(headA.val)
            headA = headA.next
        while 1: 
            if headB == None:
                break
            listB.append(headB.val)
            headB = headB.next
        
        if listA[-1] != listB[-1]:
            return None 
        
        inter = []
        for i in range(1, min(len(listA),len(listB))+1 ):
            if listA[-i] != listB[-i]:
                return ListNode(listA[-i+1])
            if i == min(len(listA),len(listB)):
                return ListNode(listA[-i])

