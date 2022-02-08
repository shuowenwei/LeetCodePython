# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-k-sorted-lists/

labuladong: https://labuladong.gitee.io/algo/1/6/

LC21, LC23, LC141, LC142, LC876, LC160, LC19


one solution: https://leetcode.com/problems/merge-k-sorted-lists/discuss/908846/Python-3-commented-O(n-log(k))-faster-than-90.64

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # if not lists:
        #     return None
        from heapq import heappush, heappop 
        # the dummy_head.next is to be returned 
        dummy_head = ListNode(-1)
        cur = dummy_head
        # initialize heap
        hp = []
        for index, ln_head in enumerate(lists):
            if ln_head:
                heappush(hp, (ln_head.val, ln_head, index)) # index is not even needed 

        # find the smallest val among the k listnodes
        while hp:
            _, node, index = heappop(hp)  # index is not even needed 
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(hp, (node.next.val, node.next, index))  # index is not even needed 
        return dummy_head.next