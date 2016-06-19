# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/palindrome-linked-list/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # solution from http://www.jiuzhang.com/solutions/palindrome-linked-list/
        # reverse the 2nd half of the linked list
        if head is None:
            return True 
        fast = slow = head
        # find the start node of the 2nd half linked list (slow) 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
            
        # reverse the 2nd half linked list 
        last = None 
        p = slow
        while p: 
            next = p.next
            p.next = last 
            last = p
            p = next 
        
        p1 = last
        p2 = head
        while p1 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
            
        # reverse the 2nd half linked list back 
        """
        last = None 
        p = last 
        while p: 
            next = p.next
            p.next = last 
            last = p
            p = next 
        """    
        return p1 is None 
        