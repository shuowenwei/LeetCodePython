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
        primes = [False]*n
        count = 0
        b = int(n**0.5)
        #i = 2 
        #while i < n:
        for i in xrange(2,n): # avoid exceeding memory limit 
            if primes[i] == False:
                count = count + 1 
                if i <= b: 
                    for j in range(i*i,n,i):
                        primes[j] = True 
        #    i = i + 1 
        return count
