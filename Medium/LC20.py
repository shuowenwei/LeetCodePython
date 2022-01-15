# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/generate-parentheses/

https://labuladong.gitee.io/algo/4/29/112/

LC698, LC78, LC46, LC77, LC22
LC51, LC37
- backtrack
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(n, start, tmp):
            if n == start:
                res.append(''.join(tmp))
                return

            for i in range(len(tmp)): # insert after position i
                tmp_copy = tmp[::]
                tmp_insert = tmp[:i] + ['(', ')'] + tmp[i:]
                # print('select:',tmp)
                backtrack(n, start+1, tmp_insert)
                tmp = tmp_copy[::]
                # print('unselect', tmp)
        backtrack(n, 1, ['(', ')'])
        return list(set(res))