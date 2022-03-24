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
        bulls, cows = 0, 0
        secret_counter = collections.Counter(secret)
        guess_counter = collections.Counter(guess)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
                secret_counter[s] -= 1
                guess_counter[g] -= 1
                
        for key, val in secret_counter.items():
            if key in guess_counter:
                cows += min(val, guess_counter[key])
        
        return str(bulls)+'A'+str(cows)+'B'