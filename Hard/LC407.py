# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/trapping-rain-water-ii/

https://leetcode.com/problems/trapping-rain-water-ii/discuss/89473/Heap-with-explanation-and-time-complexity

LC42, LC11, LC407
"""
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0:
            return 0 
        from heapq import heappop, heappush
        hp = []
        row, col = len(heightMap), len(heightMap[0])
        for i in range(row):
            heappush(hp, (heightMap[i][0], i, 0))
            heappush(hp, (heightMap[i][col - 1], i, col - 1))
        for j in range(1, col - 1):
            heappush(hp, (heightMap[0][j], 0, j))
            heappush(hp, (heightMap[row - 1][j], row - 1, j ))
        
        visited = set((i,j) for _,i,j in hp)
        res = 0
        while hp:
            h, i, j = heappop(hp)
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni = i + di
                nj = j + dj
                if (ni, nj) not in visited and ni >= 0 and nj >= 0 and ni < row and nj < col:
                    visited.add( (ni, nj) )
                    res += max(0, h - heightMap[ni][nj])
                    higherHeight = max(h, heightMap[ni][nj])
                    heappush(hp, (higherHeight, ni, nj))
        return res 
        
""" this is not working! 
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

"""