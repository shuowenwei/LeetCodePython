# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-invalid-parentheses/

https://leetcode.com/problems/remove-invalid-parentheses/discuss/75032/Share-my-Java-BFS-solution

LC20, LC921, LC1541, LC1963, LC301
-BFS
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            countLeft = 0 
            for char in s:
                if char == '(':
                    countLeft += 1
                elif char == ')':
                    countLeft -= 1
                    if countLeft < 0:
                        return False                     
            return countLeft == 0

        res = []
        visited = set()
        q = collections.deque()
        visited.add(s)
        q.append(s)
        found = False 
        while q:
            cur_s = q.popleft()
            if isValid(cur_s):
                found = True
                res.append(cur_s)
            if found:
                # check next string in the current q, but not adding any new strings 
                continue
            for i in range(len(cur_s)):
                if cur_s[i] not in ('(', ')'):
                    continue
                new_s = cur_s[:i] + cur_s[i+1:]
                if new_s not in visited:
                    visited.add(new_s)
                    q.append(new_s)
        return res 
