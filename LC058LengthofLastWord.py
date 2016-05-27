# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/length-of-last-word/

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0 
        if ' ' not in s:
            return len(s.strip()) 
            
        x = s.strip().split(' ')
        return len(x[-1]) 