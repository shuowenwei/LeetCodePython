# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-search-ii/

LC79, LC212, LC208
"""
class Solution(object):
    def exist(self, board, word):
        if len(word) == 0:
            return True
        def backtrack(board, i, j, word, visited):
            row, col = len(board), len(board[0])
            if len(word) == 0:
                return True
            if i<0 or i>=row or j<0 or j>= col or board[i][j] != word[0] or (i,j) in visited:
                return False
            visited.add((i,j))
            res = backtrack(board, i+1, j, word[1:], visited) or backtrack(board, i-1, j, word[1:], visited) or backtrack(board, i, j+1, word[1:], visited) or backtrack(board, i, j-1, word[1:], visited)
            visited.remove((i,j))
            return res 
        visited = set()
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if backtrack(board, i, j, word, visited):
                    return True
        return False 
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = [w for w in words if self.exist(board, w) is True]
        return res
