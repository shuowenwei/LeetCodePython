# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/n-queens/

https://labuladong.gitee.io/algo/1/5/

LC698, LC78, LC46, LC77, LC22, LC659
LC51, LC37, LC52
- backtracking
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
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

        res = []
        board = [['.' for i in range(n)] for j in range(n)]
        def backtracking(n, board, row):
            if row == n:
                res.append([''.join(board[i]) for i in range(n)])
            for col in range(n):
                if isValid(n, board, row, col) is False:
                    continue
                board[row][col] = 'Q'
                backtracking(n, board, row + 1)
                board[row][col] = '.'
        backtracking(n, board, 0)
        return res 
    
    
        # solution 2:rewrite
        """
        def isValid(grid, row, col):
            if 'Q' in grid[row]:
                return False
            for r in range(row):
                if grid[r][col] == 'Q':
                    return False
            r, c = row, col
            while r >=0 and c >= 0:
                if grid[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
                
            r, c = row, col
            while r >=0 and c <= n - 1:
                if grid[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            return True 
        
        res = []
        def backtracking(n, row, tmp):
            if row == n:
                res.append([''.join(tmp[i]) for i in range(n)])
                return 
            for col in range(n):
                if isValid(tmp, row, col) is False:
                    continue 
                tmp[row][col] = 'Q'
                backtracking(n, row + 1, tmp)
                tmp[row][col] = '.'
        tmp = [['.' for _ in range(n)] for _ in range(n)] 
        print(tmp)
        backtracking(n, 0, tmp)
        return res 
        """