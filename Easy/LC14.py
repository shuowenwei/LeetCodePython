# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-common-prefix/

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        
        res = ''
        # strs.sort(key = lambda x: len(x))
        for i in range(len(strs[0])):
            candidate = strs[0][i]
            for eachString in strs:
                if i > len(eachString) - 1 or candidate != eachString[i]:
                    return res 
                # if candidate != eachString[i]:
                #     return res 
            res += candidate
            
        return res
