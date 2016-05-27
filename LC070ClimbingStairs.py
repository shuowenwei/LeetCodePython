# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/climbing-stairs/

"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [] 
        for i in range(n+1):
            if i < 3 :
                results.append(i)
            else: 
                results.append( results[i-1] + results[i-2] ) 
        return results[n]