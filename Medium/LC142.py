# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/linked-list-cycle-ii/

labuladong: https://labuladong.gitee.io/algo/1/6/

LC21, LC23, LC141, LC142, LC876, LC160, LC19

LC142, LC287

LC1650, LC160, LC142
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast is not None and fast.next is not None: 
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # slow meet fast, reset slow to head
                break
        
        if fast is None or fast.next is None: # break due to condition in "while", hence no cycle
            return None
        else:
            slow = head # or fast = head
            while slow != fast:
                fast = fast.next 
                slow = slow.next
            return slow # or return fast
            