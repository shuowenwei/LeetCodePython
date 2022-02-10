# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/consecutive-numbers-sum/

https://leetcode.com/problems/consecutive-numbers-sum/discuss/128959/JavaPython-3-5-liners-O(N-0.5)-Math-method-w-explanation-and-analysis.

"""
class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # N = k + (k + 1) + (k + 2) + ... + (k + (i - 1))
        # N = k * i + (i - 1) * i / 2
        i, res = 1, 0
        while n > i * (i - 1) // 2:
            if (n - i * (i - 1) // 2) % i == 0:
                res += 1
            i += 1
        return res
    
    """
        res = 1
        i = 3
        while n % 2 == 0:
            n = n / 2
        while i*i <= n:
            cnt = 0
            while n % i == 0:
                n = n / i
                cnt += 1
            res = res * (cnt + 1)
            i += 2
        return res if n == 1 else res * 2
    """
    
