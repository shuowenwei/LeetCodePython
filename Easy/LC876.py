# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/middle-of-the-linked-list/

labuladong: https://labuladong.gitee.io/algo/1/6/

LC21, LC23, LC141, LC142, LC876, LC160, LC19

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head 
        while fast is not None and fast.next is not None: 
            fast = fast.next.next
            slow = slow.next 
        return slow 
        