# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sliding-puzzle/

https://labuladong.gitee.io/algo/4/29/114/
https://mp.weixin.qq.com/s/Xn-oW7QRu8spYzL3B6zLxw

LC111, LC752, LC773
- BFS
"""
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        row, col = len(board), len(board[0])
        start = ''.join([str(i) for i in board[0] + board[1]])
        target = '123450'
        # 1 2 3  |   0 1 2
        # 4 5 0  |   3 4 5
        def getNeighbor(state):
            dictNeighbor = {}
            dictNeighbor[state[0]] = [state[1], state[3]]
            dictNeighbor[state[1]] = [state[0], state[2], state[4]]
            dictNeighbor[state[2]] = [state[1], state[5]]
            dictNeighbor[state[3]] = [state[0], state[4]]
            dictNeighbor[state[4]] = [state[1], state[3], state[5]]
            dictNeighbor[state[5]] = [state[2], state[4]]
            return dictNeighbor
        
        def getNextState(cur_state):
            res = []
            dictNeighbor = getNeighbor(cur_state)
            for ex in dictNeighbor['0']:
                index_0 = cur_state.index('0')
                index_ex = cur_state.index(ex)
                next_state = list(cur_state)
                next_state[index_0] = ex
                next_state[index_ex] = '0'
                res.append(''.join(next_state))
            return res
        
        # 0 is moving 
        from collections import deque
        res = 0 
        visited = set()
        q = deque()
        q.append(start)
        # visited.add(start)
        while q:
            size = len(q)
            for i in range(size):
                cur_state = q.popleft()
                visited.add(cur_state) # add to visited 
                if cur_state == target: 
                    return res
                next_states = getNextState(cur_state)
                for ns in next_states:
                    if ns not in visited:
                        q.append(ns)
                        # visited.add(ns)
            res += 1
        return -1 
