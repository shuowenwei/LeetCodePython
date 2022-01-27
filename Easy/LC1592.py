# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/rearrange-spaces-between-words/

LC1592, LC68, LC2138
"""
class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        tokens = text.split()
        if len(tokens) == 1:
            return tokens[0] + ' '*(len(text) - len(tokens[0]))
        
        numSpaces = len(text) - sum(len(t) for t in tokens)
        gapLength = numSpaces / (len(tokens)-1)
        res = (' '*gapLength).join(tokens)#.replace('#', )
        return res + ' '*(len(text) - len(res))

