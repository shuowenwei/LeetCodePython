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
        res = []
        if len(digits) == 0:
            return res

        num2letter = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def backtracking(digits, path, index):
            if index == len(digits):
                res.append(''.join(path))
                return 
            letters = num2letter[int(digits[index])]
            for char in letters:
                path.append(char)
                backtracking(digits, path, index + 1)
                path.pop() 
        backtracking(digits, [], 0)
        return res 
