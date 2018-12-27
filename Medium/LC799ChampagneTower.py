# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/champagne-tower/

solution: https://leetcode.com/problems/champagne-tower/solution/

"""
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        A = [ [0]*k for k in range(1, 102) ] 
        # 102 is necessary for the input:
        # poured, query_row, query_glass = 10000, 99, 99
        # when 99th row is full, 100th row's glasses need to be calculated 
        A[0][0] = poured 
        for r in range(query_row+1):
            for c in range(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0: 
                    A[r+1][c] += q
                    A[r+1][c+1] += q
        return min(1, A[query_row][query_glass])
    