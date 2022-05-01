# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-comments/

https://leetcode.com/problems/remove-comments/discuss/109210/Simple-Python-one-pass-with-clear-inline-explanation!!!

"""
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        flag = False 
        tmp = ''
        for line in source:
            # tmp = '' # this is wrong 
            i = 0
            while i < len(line):
                if i + 1 < len(line) and line[i] == '/' and line[i+1] == '/' and flag is False:
                    i = len(line)
                elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '*' and flag is False:
                    flag = True
                    i += 1
                elif i + 1 < len(line) and line[i] == '*' and line[i+1] == '/' and flag is True:
                    flag = False
                    i += 1
                elif flag is False:
                    tmp += line[i]
                    # print(tmp)
                i += 1
            if tmp != '' and flag is False:
                res.append(tmp) 
                tmp = '' # must reset tmp here
        return res 
                
