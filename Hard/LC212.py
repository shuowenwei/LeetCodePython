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
        self.end_node = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.end_node = True
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.num_words = len(words)
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def backtracking(board, node, i, j, path, res):
            if self.num_words == 0:
                return 
            row, col = len(board), len(board[0])
            if node.end_node:
                res.append(path)
                node.end_node = False
                self.num_words -= 1

            if i<0 or i>=row or j<0 or j>= col:
                return 
            tmp = board[i][j]
            if tmp not in node.children:
                return
            board[i][j] = '#'
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                backtracking(board, node.children[tmp], i+di, j+dj, path+tmp, res)
            board[i][j] = tmp

        row, col = len(board), len(board[0])
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