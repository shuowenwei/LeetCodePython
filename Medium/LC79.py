# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-search/

"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        path = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    path.append((i,j))
        visited = []
        def getNeighbors(i,j,m,n):
            neighbors = []
            if i > 0:
                neighbors.append((i-1,j))
            if j > 0:
                neighbors.append((i,j-1))
            if i < m-1:
                neighbors.append((i+1,j))
            if j < n-1:
                neighbors.append((i,j+1))
            return neighbors
        
        res = [False]
        def backtrack(board, word, index, path):
            # print(path, '--', 'index:', index, '--')
            m, n = len(board), len(board[0])
            if index == len(word):
                res.append(True)
                return  
            if len(path) == 0:
                return 
            for (i,j) in path:
                if board[i][j] == word[index] and (i,j) not in visited:
                    # print(board[i][j], index)
                    visited.append((i,j))
                    neighbors = getNeighbors(i,j,m,n)
                    backtrack(board, word, index+1, neighbors)
                    visited.pop()
                else:
                    continue
        backtrack(board, word, 0, path)   
        return res[-1]

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

ob = Solution()
res = ob.exist(board, word)
print(res)