# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/decode-string/

https://leetcode.com/problems/decode-string/discuss/1400105/98-faster-oror-With-and-without-Stack-oror-Cleane-and-Concise

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # solution 1: using a stack 
        cur_str = ''
        num = 0
        stack = []
        for c in s:
            # c = s[i]
            if c.isdigit():
                num = 10*num + int(c)  
            elif c == '[':
                stack.append(cur_str)
                stack.append(num)
                cur_str = ''
                num = 0
            elif c == ']':
                pre_num = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + pre_num*cur_str
            else: 
                cur_str += c
        return cur_str

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