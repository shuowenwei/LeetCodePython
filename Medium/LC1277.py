# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-square-submatrices-with-all-ones/

https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)

https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441306/JavaC%2B%2BPython-DP-solution

LC221, LC1277
"""
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        res += 1
                    else:
                        new_cell_val = min(matrix[r-1][c], 
                                           matrix[r][c-1], 
                                           matrix[r-1][c-1]) + matrix[r][c]    
                        res += new_cell_val
                        matrix[r][c] = new_cell_val
        return res

        # https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441306/JavaC%2B%2BPython-DP-solution
        # 1. dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
        # 2. dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.
        # For example:
        # 1, 1, 1
        # 1, 1, 1
        # 1, 1, 1
        
        # dp[0][0] = 1
        # dp[1][1] = 2 (the square including A[1][1] can be square with element A[1][1] with size: 2 * 2, 1 * 1)
        # dp[2][2] = 3 (the square including A[2][2] can be square with element A[2][2] with size: 3 * 3, 2 * 2, 1 * 1)
        row, col = len(matrix), len(matrix[0])
        dp = matrix[::][::]
        print(dp)
        for r in range(1, row):
            for c in range(1, col):
                dp[r][c] = dp[r][c]*(min(dp[r-1][c], 
                                        dp[r][c-1], 
                                        dp[r-1][c-1]) + 1)
        print(dp)
        return sum(map(sum, dp))