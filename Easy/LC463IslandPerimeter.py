# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/island-perimeter/
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ones = [(r,c) for r in range(row) for c in range(col) if grid[r][c] == 1] 
        res = 4 * len(ones)
        for i,j in ones: 
            res = res - self.getNumNeighbours(i,j,grid)
        return res 
    
    def getNumNeighbours(self, i, j, grid):
        row, col = len(grid), len(grid[0])
        num = 0
        if i > 0:
            if grid[i-1][j] == 1:
                num += 1 
        if i < row-1:
            if grid[i+1][j] == 1:
                num += 1 
        if j > 0:
            if grid[i][j-1] == 1:
                num += 1 
        if j < col-1:
            if grid[i][j+1] == 1:
                num += 1             
        return num
    