# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/buildings-with-an-ocean-view/

"""
class Solution(object):
    def findBuildings(self, heights):
        res = 0
        max_height = 0
        n = len(heights)
        for i in range(n-1, -1, -1):
            if heights[i] > max_height:
                res += 1 
                max_height = heights[i]
                
        return res 
                
