# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-pattern/

"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patter_list = list(pattern)
        str_list = str.split(' ')
        
        if len(patter_list) != len(str_list) or len(set(patter_list)) != len(set(str_list)):
            return False 
            
        bijection = {}
        for i in range(len(patter_list)):
            if patter_list[i] not in bijection:
                bijection[patter_list[i]] = str_list[i]
            else:
                if bijection[patter_list[i]] != str_list[i]:
                    return False
        return True 