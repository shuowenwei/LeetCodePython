# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game-iii/

LC55, LC45 - greedy
LC1306, LC1345
"""
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        targets = set()
        for i, val in enumerate(arr):
            if val == 0:
                targets.add(i)
        visited = set()
        q = collections.deque()
        q.append(start)
        visited.add(start)
        while q:
            cur_index = q.popleft()
            if cur_index in targets:
                return True
            for next_index in [cur_index + arr[cur_index], cur_index - arr[cur_index]]:
                if 0 <= next_index < n and next_index not in visited:
                    q.append(next_index)
                    visited.add(next_index)
        return False 
