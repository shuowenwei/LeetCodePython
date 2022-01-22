# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/is-subsequence/submissions/

https://labuladong.gitee.io/algo/4/32/141/

LC392
- BinarySearch
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # my solution: two pointers
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if t[pt] == s[ps]:
                ps += 1
                pt += 1
            else:
                pt += 1
        return ps == len(s)        
                
