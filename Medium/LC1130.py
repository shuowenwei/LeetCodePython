# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/340004/Python-Easy-DP

"""
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp_table = {}
        def dp(arr, i, j):
            if j <= i:
                return 0
            if i + 1 == j:
                # print('ever here?')
                dp_table[(i ,j)] = arr[i] * arr[j]
                return dp_table[(i ,j)]
            if (i, j) in dp_table:
                return dp_table[(i ,j)]
            res = 2**32
            for k in range(i + 1, j + 1):
                left = dp(arr, i, k - 1) # from [i, k)
                right = dp(arr, k, j) # from [k, j]
                res = min(res, left + right + max(arr[i:k]) * max(arr[k:j+1]))
            dp_table[(i ,j)] = res 
            return res 
        
        return dp(arr, 0, len(arr) - 1)