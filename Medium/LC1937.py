# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-number-of-points-with-cost

https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344908/C%2B%2BJavaPython-3-DP-Explanation-with-pictures.

LC931, LC1937
"""
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # no need to compare everything
        row, col = len(points), len(points[0])
        if row == 1:
            return max(points[0])
        if col == 1:
            return sum(sum(col) for col in points)
        
        dp_table = points[:][:]
        for i in range(1, row):
            ########
            left, right = [0]*col, [0]*col
            left[0] = dp_table[i-1][0]
            right[col-1] = dp_table[i-1][col-1]
            for ll in range(1, col):
                left[ll] = max(left[ll - 1] - 1, dp_table[i-1][ll])
            for rr in range(col-2, -1, -1):
                right[rr] = max(right[rr + 1] - 1, dp_table[i-1][rr])
            #########
            for j in range(col):
                dp_table[i][j] = max(left[j], right[j]) + points[i][j]
        return max(dp_table[row-1])
"""
        # dp, bottom up
        row, col = len(points), len(points[0])
        dp_table = points[:][:]
        for i in range(1, row):
            for c in range(col):
                res = 0 
                for j in range(col):
                    res = max(res, points[i][c] + dp_table[i-1][j] - abs(c-j))
                dp_table[i][c] = res 
        return max(dp_table[row-1])
    
        # dp, top down 
        row, col = len(points), len(points[0])
        dp_table = {}
        def dp(points, r, c):
            if r == 0:
                dp_table[(r, c)] = points[0][c]
                return points[0][c]
            if (r, c) in dp_table:
                return dp_table[(r, c)]
            res = 0
            for j in range(col):
                res = max(res, dp(points, r-1, j) + points[r][c] - abs(j-c))
            dp_table[(r, c)] = res
            return res
        
        final_res = 0 
        for y in range(col):
            final_res = max(final_res, dp(points, row-1, y))
        print(dp_table)
        return final_res
"""