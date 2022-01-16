# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-primes/

https://labuladong.gitee.io/algo/4/30/119/

LC172, LC793, LC204, LC372
"""
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        base = 1337 
        
        # (a * b) % base = (a % base)(b % base) % base
        def mypow(a, k): # computer a**k = a * a * a * .... * a (in total k 'a')
            a = a % base
            res = 1
            for i in range(k):
                res = res * a
                res = res % base
            return res
        
        # a**[1,5,6,4] = a**4 * (a**[1,5,6])**10, hence recursion
        
        if len(b) == 0:
            return 1 
        last = b.pop()
        part1 = mypow(a, last)
        part2 = mypow(self.superPow(a, b), 10)
        
        return (part1 * part2) % base 
            
        