# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/implement-strstr/

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: 
            return 0 
        """
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1  
        """
        if len(haystack) < len(needle):
            return -1 
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i 
        return -1 
            
            
