# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-ladder/

https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95

bi-directional BFS
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or len(beginWord) != len(endWord):
            return 0

        dict_word = collections.defaultdict(list)
        wordLength = len(beginWord)        
        for word in wordList:
            for i in range(wordLength):
                s = word[:i] + '*' + word[i+1:]
                dict_word[s].append(word)
        
        # beginWord, endWord = endWord, beginWord
        visited = set()
        q_begin = collections.deque()
        q_end = collections.deque()
        q_begin.append(beginWord)
        q_end.append(endWord)
        
        # def getNeighbor(wordList, word):
        #     expectedMatchLength = len(word) - 1
        #     neighbors = []
        #     for candidateWord in wordList:
        #         if candidateWord not in visited and len(candidateWord) == len(word):
        #             numMatch = sum([cw == w for cw, w in zip(candidateWord, word)])
        #             # for wl, w in zip(w, word):
        #             #     if wl == w:
        #             #         match += 1
        #             if numMatch == expectedMatchLength:
        #                 neighbors.append(candidateWord)
        #     return neighbors
        
        step = 1
        while q_begin and q_end:
            size = len(q_begin)
            step += 1
            for i in range(size):
                cur_word = q_begin.popleft()
                for k in range(wordLength):
                    s = cur_word[:k] + '*' + cur_word[k+1:]
                    for neiWord in dict_word[s]:
                        if neiWord in q_end:
                            return step
                        if neiWord not in visited:
                            q_begin.append(neiWord)
                            visited.add(neiWord)
            if len(q_begin) > len(q_end):
                q_begin, q_end = q_end, q_begin
        return 0
