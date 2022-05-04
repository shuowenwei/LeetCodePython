# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484235/JavaC%2B%2BPython-Similar-to-LC1024

LC45, LC1024, LC1236 - greedy
"""
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        # solution 1: DP, refer to LC45, LC1024
        dp_table = [2**32] * (n+1)
        dp_table[0] = 0
        for i, rg in enumerate(ranges):
            for j in range(max(0, i-rg),  min(i+rg, n) + 1):
                dp_table[j] = min(dp_table[j], 1 + dp_table[max(0, i-rg)])
        return dp_table[n] if dp_table[n] < 2 ** 32 else - 1

        # solution 2:
        