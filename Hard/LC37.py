# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sudoku-solver/

https://labuladong.gitee.io/algo/4/29/111/

LC698, LC78, LC46, LC77
LC51, LC37
- backtrack
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        digits = '123456789'
        def getCandidates(board,i,j):
            res = []
            box_i = i/3
            box_j = j/3
            box_nums = set()
            for ii in range(3*box_i, 3+3*box_i):
                for jj in range(3*box_j, 3+3*box_j):
                    if board[ii][jj] != '.':
                        box_nums.add(board[i][j])
            row_nums = set(board[:][j])
            col_nums = set(board[i][:])
            for c in digits:
                if c not in box_nums.union(row_nums).union(col_nums):
                    res.append(c)
            return res
        
        def backtrack(board, fills, start):
            if start == len(fills):
                return True
            
            i, j = fills[start]
            list_candidates = getCandidates(board, i, j)
            for c in list_candidates:
                board[i][j] = c
                if backtrack(board, fills, start+1):
                    return True
                board[i][j] = '.'
            return False 
        
        fills = []
        for i in range(row):
            for j in range(col):
                if board[i][j] == '.':
                    fills.append((i,j))
        backtrack(board, fills, 0)
        
            