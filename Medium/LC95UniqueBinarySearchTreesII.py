# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/unique-binary-search-trees-ii/

solution: https://leetcode.com/problems/unique-binary-search-trees-ii/solution/

"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
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
            