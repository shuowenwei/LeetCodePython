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
                oneUp = s[:i-1] + str((int(s[i])+1)%10) + s[i+1:]
                oneDown = s[:i-1] + str((int(s[i])-11)%10) + s[i+1:]
                s_neighbors.append(oneUp)
                s_neighbors.append(oneDown)
            return s_neighbors            
        
        res = 0 
        q = deque()
        q.append('0000')
        while q is not None: 
            queue_size = len(q)
            for i in range(queue_size):
                cur = q.popleft()
                if cur == target:
                    return res 
                else:
                    cur_neighbors = getNextOptions(cur)
                    for cn in cur_neighbors:
                        if cn not in deadends:
                            q.append(cn)
            res += 1
        return -1