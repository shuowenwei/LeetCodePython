# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/simplify-path/

"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        tmp = ''
        for i in range(len(path)):
            char = path[i]
            # print(char, stack)
            if char != '/': 
                tmp += char
            if char == '/' or i == len(path) - 1:
                if tmp == '..':
                    if stack:
                        stack.pop()
                elif tmp in ('.', ''): # '/'
                    pass
                else:
                    stack.append(tmp)
                tmp = ''
        return '/'+'/'.join(stack)
        
