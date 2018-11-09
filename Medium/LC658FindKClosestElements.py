# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-k-closest-elements

"""
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = [] 
        if len(arr) == 1 and arr[0] ==x:
            return arr
        
        dist_arr = [(a, abs(a-x)) for a in arr] 
        dist_arr.sort(key=lambda x: x[1]) 
        for i in range(k):
            res.append(dist_arr[i][0]) 
        return sorted(res) 