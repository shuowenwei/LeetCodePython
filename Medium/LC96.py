# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/unique-binary-search-trees/

labuladong: https://labuladong.gitee.io/algo/2/18/26/

LC95, LC96, LC1373
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """ 
        # solutiion 1:
        res = [0] * (n+1)
        # n = 0, res = 1: empty tree 
        # n = 1, res = 1: root only tree
        res[0] = 1
        res[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                # 1, 2, 3, 4, ..., i-1, i (as root), i+1, ... , n
                res[i] += res[j-1] * res[i-j]
        return res[n]
        """
        # solution 2:
        memo = [[0 for i in range(n+1)] for j in range(n+1)]
        def count(low, high):
            if low >= high:
                return 1
            if memo[low][high] != 0:
                return memo[low][high]
            res = 0
            for i in range(low, high+1): 
                res += count(low, i-1) * count(i+1, high)
            memo[low][high] = res 
            return res

        return count(1, n)

        