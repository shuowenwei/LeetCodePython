# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-primes/

https://labuladong.gitee.io/algo/4/30/120/

LC172, LC793, LC204, LC372, LC268
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        # naive solution: Time Limit Exceeded --- too slow
        def isPrime(num):
            for i in range(2, int(num**0.5+1)):
                if num % i == 0:
                    return False
            return True
        res = 0 
        for i in range(2, n):
            if isPrime(i):
                res += 1
        return res
    
        # solution 2: better but not fast enough 
        res = 0 
        isPrime = [True]*n # n-1 is strintly less than n
        for i in range(2, int(n**0.5+1)):
            if isPrime[i]:
                for j in range(i*2, n, i): #<- trick happens here
                    isPrime[j] = False
        for i in range(2, n):    
            if isPrime[i]:
                res += 1 
        return res 
        """
        
        # solution 3: Sieve of Eratosthenes : O(N * loglogN)
        if n <= 2:
            return 0
        res = 0 
        isPrime = [True]*n # n-1 is strintly less than n
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(n**0.5+1)):
            if isPrime[i]:
                for j in range(i*i, n, i): #让 j 从 i 的平方开始遍历，而不是从 2 * i 开始：
                    isPrime[j] = False
        return sum(isPrime) 
