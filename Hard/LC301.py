# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-invalid-parentheses/

https://leetcode.com/problems/remove-invalid-parentheses/discuss/75032/Share-my-Java-BFS-solution

LC20, LC921, LC1541, LC1963, LC301
-BFS

LC301 vs LC1249
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
        keeySearchFlag = True 
        while q:
            cur_s = q.popleft()
            if isValid(cur_s):
                res.append(cur_s)
                keeySearchFlag = False
            if keeySearchFlag:
                for i in range(len(cur_s)):
                    if cur_s[i] not in ('(', ')'): # only remove '(' or ')', e.g. '(a)())'
                        continue
                    new_s = cur_s[:i] + cur_s[i+1:]
                    if new_s not in visited: # prune, e.g.: '())))))))))))))....)'
                        visited.add(new_s)
                        q.append(new_s)
        return res 
