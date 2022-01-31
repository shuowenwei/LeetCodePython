# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

"""
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        def getLargerNeighbors(matrix, i,j):
            largerNieghbors = []
            cur = matrix[i][j]
            if i > 0 and matrix[i-1][j] > cur:
                largerNieghbors.append((i-1, j))
            if j > 0 and matrix[i][j-1] > cur:
                largerNieghbors.append((i, j-1))
            if i < row-1 and matrix[i+1][j] > cur:
                largerNieghbors.append((i+1, j))
            if j < col-1 and matrix[i][j+1] > cur:
                largerNieghbors.append((i, j+1))
            return largerNieghbors
        
        graph = {}
        sorted_values = []
        for i in range(row):
            for j in range(col):
                sorted_values.append((matrix[i][j], i, j))
                graph[(i, j)] = getLargerNeighbors(matrix, i,j)
        
        # print(graph)
        sorted_values.sort(key=lambda x: x[0])
        started = set()
        dp_table = {}
        def dfs(i, j):
            if (i, j) in dp_table:
                return dp_table[(i, j)]
            res = 1
            if len(graph[(i, j)]) == 0:
                return res
            else:
                for ni, nj in graph[(i, j)]:
                    started.add((ni,nj))
                    res = max(res, 1 + dfs(ni, nj))
            dp_table[(i, j)] = res
            return res
        final_res = 1
        for s in sorted_values:
            val, i, j = s
            if (i,j) not in started:
                final_res = max(final_res, dfs(i,j) )
        return final_res