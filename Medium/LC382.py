# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/linked-list-random-node/

https://labuladong.gitee.io/algo/4/30/119/

LC382, LC398
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head 
        
    def getRandom(self):
        """
        :rtype: int
        """
        from random import randint
        p = self.head
        i = 0 
        res = 0 
        while p is not None:
            i += 1 
            # // 生成一个 [0, i) 之间的整数
            # // 这个整数等于 0 的概率就是 1/i
            if randint(0, i-1) == 0: # randint(a,b) returns a uniformly random num between [a,b] 
                res = p.val
            p = p.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()