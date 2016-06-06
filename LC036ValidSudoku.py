# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-sudoku/

"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        grid = [set() for i in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue 
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                g = r/3*3 + c/3
                if board[r][c] in grid[g]:
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                grid[g].add(board[r][c])
                
        return True 
        
        