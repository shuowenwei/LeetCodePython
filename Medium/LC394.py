# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/decode-string/

https://leetcode.com/problems/decode-string/discuss/1400105/98-faster-oror-With-and-without-Stack-oror-Cleane-and-Concise

time and space complexity is O(m), where m is size of our answer

LC726, LC394
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # solution 1: using a stack 
        stack = []
        num = 0
        res = ''
        for i, char in enumerate(s):
            if char.isdigit():
                num = 10*num + int(char)
            elif char == '[':
                stack.append(res)
                stack.append(num)
                res = ''
                num = 0
            elif char == ']': # "3[a2[c]]"
                pre_num = stack.pop()
                pre_str = stack.pop() 
                res = pre_str + pre_num * res
            else:
                res += char 
        return res

        # solution 2: recursive 
        def dfs(s, p):
            res = ''
            num = 0 
            i = p
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = 10*num + int(c)  
                elif c == '[':
                    local, pos = dfs(s, i+1)
                    res += local*num
                    i = pos 
                    num = 0
                elif c == ']':
                    return res, i
                else:                
                    res += c
                i += 1
            return res, i
        return dfs(s,0)[0]
        # print(i)
        # print(res)