# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/4-keys-keyboard/

https://labuladong.gitee.io/algo/3/25/93/

LC650, LC651
"""
class Solution(object):
    def maxA(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_table = [0] * (n+1)
        dp_table[0] = 0
        for i in range(1, n+1):
            dp_table[i] = dp_table[i-1] + 1
            for j in range(2, i):
                # // 全选 & 复制 dp[j-2]，连续粘贴 i - j 次
                # // 屏幕上共 dp[j - 2] * (i - j + 1) 个 A
                dp_table[i] = max(dp_table[i], dp_table[j-2]*(i-j+1))
        return dp_table[n]
