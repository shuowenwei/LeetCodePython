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
        # solution from https://leetcode.com/discuss/105410/beats-python-solution-using-stack-complexity-space-complexity 
        # Python solution using a stack with O(N) time complexity and O(N/2) space complexity 
        if not head or not head.next: 
            return True 
        stack = [] 
        fast = slow = current = head 
        # get the midpoint (slow) 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
            
        # push the 2nd hal into the stack 
        stack.append(slow.val) 
        while slow.next: 
            slow = slow.next
            stack.append(slow.val) 
        
        # comparison
        while stack: 
            if stack.pop() != current.val:
                return False
            current = current.next 
        return True 
            
        