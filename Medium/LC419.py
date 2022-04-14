# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/battleships-in-a-board/

LC419, LC200
"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    # Battleships can only be placed horizontally or vertically on board
                    if i > 0 and board[i-1][j] == "X" or j > 0 and board[i][j-1] == "X":
                        continue
                    res += 1
        return res

        # solution 2, refer to LC200 number of islands, using DFS 
        grid = board
        if len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        def dfs(grid, i, j):
            if i < 0 or i > row-1 or j < 0 or j > col - 1 or grid[i][j] != 'X':
                return 
            grid[i][j] = '#' # flood it
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
              
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'X':
                    res += 1
                    dfs(grid, i, j)
        return res