# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/dungeon-game/

https://labuladong.gitee.io/algo/3/26/85/

LC931, LC64, LC174, LC514
"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        grid = dungeon
        row, col = len(grid), len(grid[0])
        # 从 grid[i][j] 到达终点（右下角）所需的最少生命值是 dp(grid, i, j)。
        dp_table = [[-1 for i in range(col)] for j in range(row)]
        def dp(grid, i, j):
            row, col = len(grid), len(grid[0])
            if i == row-1 and j == col-1:
                return 1 if grid[i][j] >= 0 else -grid[i][j]+1
            if i == row or j == col:
                return 2**31-1 
            if dp_table[i][j] != -1: 
                return dp_table[i][j]
            # // 状态转移逻辑
            res = min(dp(grid, i+1, j),
                      dp(grid, i, j+1)) - grid[i][j]
            # // 骑士的生命值至少为 1
            dp_table[i][j] = 1 if res <= 0 else res
            return dp_table[i][j]
        return dp(dungeon, 0, 0)
    
