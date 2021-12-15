# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/surrounded-regions/

https://labuladong.gitee.io/algo/2/19/38/

LC323, LC130, LC990

"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # solution 1: BFS via queue
        from collections import deque 
        rowNum, colNum = len(board), len(board[0])
        # get all 'O' on the 4 edges and put in a qeueu
        edgeO1 = [(i,j) for i in range(rowNum) for j in [0, colNum-1] if board[i][j] == 'O']
        edgeO2 = [(i,j) for i in [0, rowNum-1] for j in range(colNum) if board[i][j] == 'O']
        q = deque(edgeO1 + edgeO2)
        while q: 
            i,j = q.popleft()
            if board[i][j] == 'O':
                board[i][j] = '#'
                # add all its neighbors to queue and check 
                if i > 0: 
                    q.append((i-1, j))
                if j > 0: 
                    q.append((i, j-1))
                if i < rowNum-1: 
                    q.append((i+1, j))
                if j < colNum-1: 
                    q.append((i, j+1))

        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j]== 'O':
                    board[i][j] = 'X'
                elif board[i][j]== '#':
                    board[i][j] = 'O'
                    
        """ solution 2: DFS
        rowNum, colNum = len(board), len(board[0])
        edgeO1 = [(i,j) for i in range(rowNum) for j in [0, colNum-1] if board[i][j] == 'O']
        edgeO2 = [(i,j) for i in [0, rowNum-1] for j in range(colNum) if board[i][j] == 'O']        
        def dfs(board,i,j):
            if board[i][j] == 'O':
                board[i][j] = '#'
                if i > 0: 
                    dfs(board,i-1,j)
                if j > 0: 
                    dfs(board,i,j-1)
                if i < rowNum-1: 
                    dfs(board,i+1,j)
                if j < colNum-1:
                    dfs(board,i,j+1)
                    
        for i,j in edgeO1+edgeO2:
            dfs(board,i,j)
            
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j]== 'O':
                    board[i][j] = 'X'
                elif board[i][j]== '#':
                    board[i][j] = 'O'
        """            
