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
        
        if len(patter_list) != len(str_list) or len(set(patter_list)) != len(set(str_list)): # "abba" vs "dog dog dog dog"
            return False 
            
        bijection = {}
        for i in range(len(patter_list)):
            if patter_list[i] not in bijection:
                bijection[patter_list[i]] = str_list[i]
            else:
                if bijection[patter_list[i]] != str_list[i]:
                    return False
        return True 

        """
        # my later longer and uglier solution: 
        dict_pattern = {}
        dict_s = {}
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False 
        for pp, ss in zip(pattern, s_list):
            if pp not in dict_pattern:
                dict_pattern[pp] = ss
            else:
                if dict_pattern[pp] != ss:
                    return False
            # "abba" vs "dog dog dog dog"
            if ss not in dict_s:
                dict_s[ss] = pp
            else:
                if dict_s[ss] != pp:
                    return False
        return True
        """