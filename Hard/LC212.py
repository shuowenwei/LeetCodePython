# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-search-ii/

LC79, LC212
LC208, LC1804, LC648, LC211

https://leetcode.com/problems/word-search-ii/discuss/712733/Python-Trie-solution-with-dfs-explained
"""
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curNode = self.root
        for char in word:
            curNode = curNode.children[char]
        curNode.is_end = True
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        row, col = len(board), len(board[0])
        def backtracking(board, node, i, j, path, res):
            if node.is_end:
                res.append(path)
                node.is_end = False # prevent over-counting
            if i<0 or i>=row or j<0 or j>= col:
                return            
            tmp = board[i][j]
            if tmp not in node.children:
                return 
            board[i][j] = '#'
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                backtracking(board, node.children[tmp], i+di, j+dj, path+tmp, res)
            board[i][j] = tmp

        for i in range(row):
            for j in range(col):
                backtracking(board, trie.root, i, j, '', res)
        return res 
    
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
        res = [w for w in words if self.exist(board, w) is True]
        return res
""" 