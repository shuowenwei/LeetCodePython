# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/bulls-and-cows/

"""

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s_secret = list(str(secret))
        s_guess = list(str(guess))
        bulls = 0
        cows = 0
        for i in range(len(s_secret)): 
            if s_guess[i] == s_secret[i] :
                bulls += 1
        for c in s_guess:
            if c in s_secret: 
                cows += 1
                s_secret.remove(c)
        cows = cows - bulls 
        return str(bulls)+'A'+str(cows)+'B'