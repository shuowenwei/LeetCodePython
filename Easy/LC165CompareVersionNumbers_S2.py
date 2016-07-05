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
        i=j=0 
        v1_num = v2_num = 0 
        while i<len(version1) or j<len(version2):
            while ( i<len(version1) and version1[i] != '.'):
                v1_num = v1_num * 10 + int(version1[i])
                i += 1 
            while ( j<len(version2) and version2[j] != '.'):
                v2_num = v2_num * 10 + int(version2[j])
                j += 1 
            if v1_num > v2_num:
                return 1 
            elif v1_num < v2_num:
                return -1
            v1_num = v2_num = 0 
            i += 1 
            j += 1
        return 0 
                