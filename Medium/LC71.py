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
        folder = ''
        for i, char in enumerate(path):
            if char != '/':
                folder += char 
            if char == '/' or i == len(path) - 1:
                if folder == '..':
                    if stack:
                        stack.pop()
                # must use elif: e.g. '/../'
                elif folder in ('', '.'):
                    pass
                # must use elif 
                else:
                    stack.append(folder)
                folder = ''
            # print(stack)
        return '/' + '/'.join(stack)
        
