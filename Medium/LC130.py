# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/surrounded-regions/

https://labuladong.gitee.io/algo/2/19/38/

LC323, LC130, LC990

"""
class Solution: 
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # BFS 
        if len(board) == 0 or len(board[0]) == 0: return
        
        self.row, self.col = len(board), len(board[0])
        borderOs = [(i,j) for i in range(self.row) for j in range(self.col) 
                    if (i == 0 or j == 0 or i == self.row-1 or j == self.col-1) 
                    and board[i][j]== 'O']
        queue = collections.deque(borderOs)
        while queue:
            i, j = queue.popleft()
            if 0<=i<self.row and 0<=j<self.col and board[i][j] == 'O':
                board[i][j] = '*'
                queue.append((i-1,j))
                queue.append((i+1,j))
                queue.append((i,j-1))
                queue.append((i,j+1))
                
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j]== 'O':
                    board[i][j] = 'X'
                elif board[i][j]== '*':
                    board[i][j] = 'O' 
                    