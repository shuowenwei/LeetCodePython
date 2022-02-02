# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/guess-the-word/

https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison

"""
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def match(self, w1, w2):
        res = 0
        for l1, l2 in zip(w1, w2):
            if l1 == l2:
                res += 1
        return res 

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        from collections import defaultdict, Counter
        import random
        for i in range(10):
            gs = random.choice(wordlist)
            x = master.guess(gs)
            wordlist = [w for w in wordlist if self.match(w, gs) == x]

