# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sudoku-solver/

https://labuladong.gitee.io/algo/4/29/111/

LC698, LC78, LC46, LC77, LC22, LC659
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
        def getCandidates(board,i,j):
            res = []
            box_i = i/3
            box_j = j/3
            box_nums = set()
            for bi in range(3*box_i, 3+3*box_i):
                for bj in range(3*box_j, 3+3*box_j):
                    if board[bi][bj] != '.':
                        box_nums.add(board[bi][bj])
            row_nums = set(board[i][:])
            col_nums = set([board[cj][j] for cj in range(9)]) # this is different from set(board[:][j])
            # print('\t', box_nums, row_nums, col_nums)
            for c in '123456789':
                if c not in box_nums and c not in row_nums and c not in col_nums:
                    res.append(c)
            return res
        
        def backtrack(board, fills, start):
            if start == len(fills):
                return True
            
            i, j = fills[start]
            list_candidates = getCandidates(board[::], i, j)
            for c in list_candidates:
                # print(i, j, start, 'choose -->', c, 'from', list_candidates)
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
        # print(fills, len(fills))
        res = backtrack(board, fills, 0)
        # print('res', res)
        