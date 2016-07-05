# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/compare-version-numbers/

"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def convert2Integer(numString):
            res=0 
            for i in numString:
                res = res*10 + int(i)
            return res 
        v1_list = version1.split('.')    
        v2_list = version2.split('.')
        max_lex = max(len(v1_list),len(v2_list))
        
        i=j=0 
        v1_num = v2_num = 0 
        
        while i<len(v1_list) or j<len(v2_list):
            if i >= len(v1_list):
                v1_num = 0
            else:
                v1_num = convert2Integer(v1_list[i])
            if j >= len(v2_list):
                v2_num = 0 
            else:
                v2_num = convert2Integer(v2_list[i])
            if v1_num > v2_num:
                return 1 
            elif v1_num < v2_num:
                return -1
            v1_num = v2_num = 0 
            i = i + 1 
            j = j + 1
        return 0 
                