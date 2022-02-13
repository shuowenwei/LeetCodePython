# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num2letter = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        if digits == '':
            return res 
        def backtracking(digits, index, tmp):
            if len(digits) == index:
                res.append(''.join(tmp))
                return
            for char in num2letter[int(digits[index])]:
                tmp.append(char)
                backtracking(digits, index + 1, tmp)
                tmp.pop()
        backtracking(digits, 0, [])
        return res 
