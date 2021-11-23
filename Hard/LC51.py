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
            # 检查列是否有皇后互相冲突
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # 检查左上方是否有皇后互相冲突
            for i,j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            # 检查右上方是否有皇后互相冲突
            for i,j in zip(range(row-1, -1, -1), range(col+1, n, +1)):
                if board[i][j] == 'Q':
                    return False
            return True

        def putQueens(n, board, row):
            if row == n:
                res.append([''.join(board[i][:]) for i in range(n)])
                return 
            for col in range(n):
                if isValid(n, board, row, col) is False:
                    continue 
                board[row][col] = 'Q'
                putQueens(n, board, row+1)
                board[row][col] = '.'
        putQueens(n, board, 0)
        return res