# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/magic-squares-in-grid
"""
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import Counter 
        target = [1,2,3,4,5,6,7,8,9]
        tCounter = Counter(target)
        
        res = 0 
        if len(grid) < 3 or len(grid[0]) < 3: 
            return res 
        
        for i in range(len(grid)-2):
            cand = [] 
            for j in range(len(grid[0])-2): 
                cand = grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3] 
                # row wise
                if sum(grid[i][j:j+3]) != 15 or sum(grid[i+1][j:j+3]) != 15 or sum(grid[i+2][j:j+3]) != 15:
                    continue  
                # column wise 
                if grid[i][j] + grid[i+1][j] + grid[i+2][j] != 15 or grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != 15 or grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != 15:
                    continue 
                # diagnal wise 
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15 or grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15:
                    continue
                gCounter = Counter(cand)
                if tCounter == gCounter: 
                    res += 1 
        return res 
                