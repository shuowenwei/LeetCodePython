# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

"""

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        """
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1 
        return arr 
        """
        res = [-1]
        max_num = 0 
        for e in arr[::-1]:
            max_num = max(max_num, e)
            res.append(max_num)
        return res[::-1][1:]