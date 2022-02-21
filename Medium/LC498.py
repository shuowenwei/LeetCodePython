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
        # https://leetcode.com/problems/diagonal-traverse/discuss/97767/Simply-Python-Solution
        result = []
        dd = collections.defaultdict(list)
        if not mat: 
            return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                dd[i+j+1].append(mat[i][j]) # starting indices from 1, hence i+j+1.
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        # print(dd)
        for k in sorted(dd.keys()):
            if k % 2==1: dd[k].reverse()
            result += dd[k]
        return result

        # my long and ugly solution: 
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
