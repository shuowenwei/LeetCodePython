# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/diagonal-traverse/

"""
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(mat) == 0:
            return res 
        row, col = len(mat), len(mat[0])
        # Numbers in same diagonal have same value of row+col
        d = {}
        for i in range(row):
            for j in range(col):
                if i+j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        # Place diagonals in the result list. But remember to reverse numbers in odd diagonals
        for key in sorted(d.keys()):
            if key % 2 == 0:
                res += d[key][::-1]
            else:
                res += d[key]
        return res 


        # Solution 2: my long and ugly solution: 
        direction = 'upRight' # 'downLeft'
        row, col = len(mat), len(mat[0])
        q = collections.deque()
        q.append((0,0))
        res = []
        while len(res) < row * col:
            r, c = q.popleft()
            # print(direction, r, c)
            res.append(mat[r][c])
            if direction == 'upRight':
                nr, nc = r-1, c+1
                if nr >= 0 and nc <= col - 1:
                    q.append((r-1, c+1))
                elif nc <= col - 1:
                    q.append((r, c+1))
                    direction = 'downLeft'
                else:
                    q.append((r+1, c))
                    direction = 'downLeft'
            elif direction == 'downLeft':
                nr, nc = r+1, c-1
                if nc >= 0 and nr <= row - 1:
                    q.append((r+1, c-1))
                elif nr <= row - 1:
                    q.append((r+1, c))
                    direction = 'upRight'
                else:
                    q.append((r, c+1))
                    direction = 'upRight'
        return res
