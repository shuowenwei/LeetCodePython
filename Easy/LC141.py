# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/linked-list-cycle/

https://labuladong.github.io/algo/2/19/18/

LC21, LC23, LC141, LC142, LC876, LC160, LC19, LC86
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
