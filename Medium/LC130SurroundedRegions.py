# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/surrounded-regions/

"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0: return
        
        self.board = board
        self.row, self.col = len(self.board), len(self.board[0])
        edge_points = [(i,j) for i in range(self.row) for j in range(self.col) if 
                       i == 0 or j == 0 or i == self.row-1 or j == self.col-1]
        # print(edge_points)
        self.res = [[1 for i in range(self.col)] for j in range(self.row)] 
        for (i,j) in edge_points:
            self.DFS(i, j)
                
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j]== 'O' and self.res[i][j] == 1:
                    board[i][j] = 'X'
                    
    def DFS(self, i, j):
        if i < 0 or i >= self.row: return 
        if j < 0 or j >= self.col: return 
        if self.board[i][j] != 'O': return 
        if self.res[i][j] == 0: return # just in case input: [["O","O"],["O","O"]]
        
        self.res[i][j] = 0
        
        self.DFS(i-1, j)
        self.DFS(i, j-1)
        self.DFS(i+1, j)
        self.DFS(i, j+1)
        