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
        n = len(arr)
        if n <= 1:
            return 0 
        dict_index = {}
        for i, a in enumerate(arr):
            if a in dict_index:
                dict_index[a].append(i)
            else:
                dict_index[a] = [i]
        res = [2**32] * n
        res[0] = 0
        # BFS
        from collections import deque 
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        while q:
            cur_index = q.popleft()
            if cur_index == n-1:
                return res[cur_index]
            if arr[cur_index] in dict_index:
                for next_index in dict_index[arr[cur_index]]:
                    if next_index not in visited:
                        visited.add(next_index)
                        res[next_index] = res[cur_index] + 1 
                        q.append(next_index)
                # very very important to avoid double calculating 
                del dict_index[arr[cur_index]]

            if cur_index + 1 < n and cur_index + 1 not in visited:
                visited.add(cur_index + 1)
                res[cur_index+1] = res[cur_index] + 1
                q.append(cur_index+1)
                
            if cur_index - 1 >= 0 and cur_index - 1 not in visited:
                visited.add(cur_index - 1)
                res[cur_index-1] = res[cur_index] + 1
                q.append(cur_index-1)
                
