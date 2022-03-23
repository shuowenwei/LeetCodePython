# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/jump-game-iv/

LC55, LC45 - greedy
LC1306, LC1345
"""
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        import collections 
        n = len(arr)
        if n <= 1:
            return 0 
        dict_index = collections.defaultdict(list)
        for i, val in enumerate(arr):
            dict_index[val].append(i)
        # BFS
        from collections import deque 
        q = deque()
        visited = set()
        step = 0
        q.append((0, step))
        visited.add(0)
        while q:
            cur_index, step = q.popleft()
            if cur_index == n-1:
                return step
            for next_index in set(dict_index[arr[cur_index]] + [cur_index + 1, cur_index - 1]):
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    q.append((next_index, step + 1)) 
            # very very important to avoid double calculating 
            del dict_index[arr[cur_index]]
                
