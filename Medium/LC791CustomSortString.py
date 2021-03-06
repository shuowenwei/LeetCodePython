# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/custom-sort-string/

solution: https://leetcode.com/problems/custom-sort-string/discuss/126559/Easy-Python-Solution

"""
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = [] 
        
        for s in S:
            res.append(s*T.count(s))
        for t in T:
            if t not in S:
                res.append(t)
        return ''.join(res)
          