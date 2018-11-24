# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

solution reference: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/139609/python-iterative-and-recursive-solution


"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        stack = [s]
        res = 0 
        while stack: 
            ss = stack.pop()
            allCharAreGood = True
            for c in set(ss):
                if ss.count(c) < k: 
                    stack.extend([z for z in ss.split(c)]) 
                    allCharAreGood = False 
                    break
            if allCharAreGood: #else: 
                res = max(res, len(ss)) # if allCharAreGood in ss, then len(ss)
        return res 
        
        """ recursive 
        res = 0 
        if not s or len(s) < k:
            return res 
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        # if every char in s appears >= k time, then the whole string is OK 
        return len(s)
        """
        