# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-primes/

"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3: 
            return 0 
        primes = [True for i in range(n)]
        primes[0] = False 
        primes[1] = False 
        i = 2 
        while i**2 <= n-1: 
            if primes[i] == True:
                for j in range(i,(n-1)/i+1):
                    primes[i*j] = False
            i = i + 1
        return primes.count(True)
        
