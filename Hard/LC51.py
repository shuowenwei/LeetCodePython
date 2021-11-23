# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/n-queens/

labuladong: https://labuladong.gitee.io/algo/1/4/

"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [['.' for i in range(n)] for j in range(n)]
        
        def isValid(n, board, row, col):
            for i in range(n):
                if board[i].count('Q') > 1:
                    return False 
                if board[:][i].count('Q') > 1:
                    return False
            for i in range(n):
                for j in range(n):
                    if abs(row-i) == abs(col-j) and row != i and board[i][j] == 'Q': 
                        return False
            return True

        def putQueens(n, board, row):
            if row == n-1:
                res.append([''.join(board[i][:]) for i in range(n)])
                # print(res)
                return 
            for col in range(n):
                if isValid(n, board, row, col) is False:
                    continue 
                board[row][col] = 'Q'
                putQueens(n, board, row+1)
                board[row][col] = '.'                        
        putQueens(n, board, 0, 0)
        return res 
    # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]