# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-two-sorted-lists/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2 
        if l2 is None:
            return l1 
        headOne = l1
        headTwo = l2

        newHead = None 
        
        if headOne.val <= headTwo.val:
            newHead = headOne 
            headOne = headOne.next
        else: 
            newHead = headTwo  
            headTwo = headTwo.next
        r = newHead 
        while headOne and headTwo:
            if headOne.val <= headTwo.val: 
                r.next = headOne
                headOne = headOne.next
            else: 
                r.next = headTwo
                headTwo = headTwo.next
            r=r.next 
           
        if headOne is None and headTwo is not None:
            r.next = headTwo
            
        if headTwo is None and headOne is not None:
            r.next = headOne 
            
        return newHead 

