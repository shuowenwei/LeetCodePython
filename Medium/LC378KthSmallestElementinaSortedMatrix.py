# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

kinda of cheating ...

"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        n = len(matrix) 
        if n == 1: 
            return matrix[0][0]
        num = []
        for i in range(n):
            num.extend(matrix[i])
        num = sorted(num)
        return num[k-1]
