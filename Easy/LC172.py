# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/factorial-trailing-zeroes/

https://labuladong.gitee.io/algo/4/30/117/

LC172, LC793
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # my solution
        # 比如说 n = 25，那么 25! 最多可以分解出几个 2 和 5 相乘？这个主要取决于能分解出几个因子 5，因为每个偶数都能分解出因子 2，因子 2 肯定比因子 5 多得多。
        # divisorFive = [0]*n
        totalFives = 0 
        for i in range(1, n+1):
            while i % 5 == 0:
                i = i/5 
                # divisorFive[i-1] += 1
                totalFives += 1
        return totalFives
    
        #solution 2: a little bit faster
        totalFives = 0 
        while n > 0: 
            n = n / 5
            totalFives += n
        
        # solution 3: only 5, 25, 125...can increase the 0 numbers.
        if n < 5:
             return 0
        # elif n == 5 :
        #     return 1 
        else: 
            totalFives = 0
            i = 1 
            while n >= 5**i: 
                totalFives +=  n/(5**i)
                i += 1
        return totalFives