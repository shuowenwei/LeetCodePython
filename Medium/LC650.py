# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/2-keys-keyboard/

LC650, LC651
"""
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def getLargestDivisor(n):
            for d in range(n//2, 0, -1):
                if n % d == 0:
                    return d # could be 1, hence a prime number
        res = [n+1]*(n+1)
        res[1] = 0
        # res[2] = 2 # 2 is prime
        # res[3] = 3 # 3 is prime
        for i in range(2, n+1):
            ld = getLargestDivisor(i)
            if ld == 1: # this is a prime number
                res[i] = i
            else:
                para = i/ld
                res[i] = min(res[i], res[ld]+1+para-1) # copy 1 time, paste (para-1) times
        # print(res)
        return res[n]