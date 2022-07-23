# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/middle-of-the-linked-list/

https://labuladong.github.io/algo/2/19/18/

LC21, LC23, LC141, LC142, LC876, LC160, LC19, LC86
LC876, LC148
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
        # 需要注意的是，如果链表长度为偶数，也就是说中点有两个的时候，我们这个解法返回的节点是靠后的那个节点。
        return slow