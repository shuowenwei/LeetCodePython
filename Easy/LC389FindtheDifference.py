# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-the-difference/

"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list_t = list(t)
        for e in s:
            list_t.remove(e)
        return list_t[0]



class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Solution 1: 
        # s_counter = collections.Counter(s)
        # for e in t:
        #     if e not in s_counter:
        #         return e 
        #     else:
        #         s_counter[e] -= 1 
        #         if s_counter[e] < 0:
        #             return e 
        
        # Solution 2: 
        return list((collections.Counter(t) - collections.Counter(s)))[0]