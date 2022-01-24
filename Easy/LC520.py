# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/detect-capital/submissions/

"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        captitalA = ord('A')
        captitalZ = ord('Z')
        n = len(word)
        firstLetter = ord(word[0])
        secondLetter = ord(word[1])
        # first letter is not captital, then all must be lower case
        if not (captitalA <= firstLetter <= captitalZ):
            # print('here1', firstLetter, captitalA <= firstLetter <= captitalZ)
            for i in range(1, n):
                if captitalA <= ord(word[i]) <= captitalZ:
                    return False
        # first letter is captital
        # 1. second letter is captial, all must be captital
        elif captitalA <= secondLetter <= captitalZ:
            # print('here2')
            for i in range(2, n):
                if not (captitalA <= ord(word[i]) <= captitalZ):
                    return False
        # 2. second letter is not captial, rest must not be captital
        else:
            print('here3')
            for i in range(2, n):
                if captitalA <= ord(word[i]) <= captitalZ:
                    return False
        return True 
