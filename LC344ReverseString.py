# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-string/

"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=1:
            return s
            
        res = ''
        list_str = list(s)
        for i in range(len(s)/2):
            temp = list_str[i]
            list_str[i] = list_str[len(s)-1-i]
            list_str[len(s)-1-i] = temp 
            
        return str(''.join(list_str))
            