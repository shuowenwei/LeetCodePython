# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/open-the-lock/

"""
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        from collections import deque
        def getNextOptions(s):
            s_neighbors = []
            for i in range(len(s)):
                oneUp, oneDown = list(s), list(s)
                oneUp[i] = str((int(s[i])+1)%10)
                oneDown[i] = str((int(s[i])-1)%10)
                s_neighbors.append(''.join(oneUp))
                s_neighbors.append(''.join(oneDown))
            return s_neighbors
        
        res = 0 
        q = deque()
        visited = set()
        q.append('0000')
        
        while len(q) > 0:
            queue_size = len(q)
            for i in range(queue_size):
                cur = q.popleft()
                if cur in deadends:
                    continue
                elif cur == target:
                    return res
                else:
                    cur_neighbors = getNextOptions(cur)
                    # print(cur, ':', cur_neighbors)
                    for cn in cur_neighbors:
                        if cn not in visited: # wrong: cn not in deadends and ...
                            q.append(cn)
                            visited.add(cn)
            res += 1
        return -1