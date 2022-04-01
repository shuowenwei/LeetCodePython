# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-search/

https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

LC79, LC212
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
        
        self.res = False
        def backtrack(board, word, index, path):
            # print(path, '--', 'index:', index, '--')
            m, n = len(board), len(board[0])
            if index == len(word):
                self.res = True
                return
            # if len(path) == 0:
            #     return 
            for (i,j) in path:
                if board[i][j] == word[index] and (i,j) not in visited:
                    # print(board[i][j], index)
                    visited.append((i,j))
                    neighbors = getNeighbors(i,j,m,n)
                    backtrack(board, word, index+1, neighbors)
                    visited.pop()

        backtrack(board, word, 0, path)   
        return self.res

        # solution refer to 
        # https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
        if len(word) == 0:
            return True
        
        def backtrack(board, i, j, word, visited):
            if len(word) == 0:
                return True
            if i<0 or i>=row or j<0 or j>= col or board[i][j] != word[0] or (i,j) in visited:
                return False
            visited.add((i,j))
            # if backtrack(board, i+1, j, word[1:], visited) or backtrack(board, i-1, j, word[1:], visited) or backtrack(board, i, j+1, word[1:], visited) or backtrack(board, i, j-1, word[1:], visited):
            #     return True
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                if backtrack(board, i + di, j + dj, word[1:], visited):
                    return True
            visited.remove((i,j))

        visited = set()
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if backtrack(board, i, j, word, visited):
                    return True
        return False 



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

ob = Solution()
res = ob.exist(board, word)
print(res)