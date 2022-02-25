# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-pattern/

"""
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern = list(pattern)
        s_list = s.split(' ')
        if len(s_list) != len(pattern) or len(set(s_list)) != len(set(pattern)):# "abba" vs "dog dog dog dog"
            return False
        
        dict_bijection = {}
        for pp, ss in zip(pattern, s_list):
            if pp not in dict_bijection:
                dict_bijection[pp] = ss
            else:
                if dict_bijection[pp] != ss:
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