# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/trapping-rain-water-ii/

LC42, LC11, LC407
"""
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        row, col = len(heightMap), len(heightMap[0])
        
        import numpy as np 
        leftHeightMap = np.zeros((row, col))
        rightHeightMap = np.zeros((row, col))
        upHeightMap = np.zeros((row, col))
        downHeightMap = np.zeros((row, col))
        
        for i in range(row):
            curMax = 0 
            for j in range(col):
                if heightMap[i][j] > curMax:
                    curMax = heightMap[i][j]
                leftHeightMap[i][j] = curMax
        
        for i in range(row):
            curMax = 0 
            for j in range(col-1, -1, -1):
                if heightMap[i][j] > curMax:
                    curMax = heightMap[i][j]
                rightHeightMap[i][j] = curMax
        
        for j in range(col):
            curMax = 0 
            for i in range(row):
                if heightMap[i][j] > curMax:
                    curMax = heightMap[i][j]
                upHeightMap[i][j] = curMax
        
        for j in range(col):
            curMax = 0 
            for i in range(row-1, -1, -1):
                if heightMap[i][j] > curMax:
                    curMax = heightMap[i][j]
                downHeightMap[i][j] = curMax
        res = 0 
        for i in range(row):
            for j in range(col):
                res += max(0, min(leftHeightMap[i][j], 
                                  rightHeightMap[i][j],
                                  upHeightMap[i][j],
                                  downHeightMap[i][j]) - heightMap[i][j])
                # if tmp > 0:
                #     print(i,j,tmp)
                #     print(leftHeightMap[i][j])
                #     print(rightHeightMap[i][j])
                #     print(upHeightMap[i][j])
                #     print(leftHeightMap[i][j])
                # res += tmp 
        # print(leftHeightMap)
        # print(rightHeightMap)
        return int(res)

