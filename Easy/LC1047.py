# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

"""
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # refer to https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/294893/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        
        # solution 3: Time Limit Exceeded
        if len(s) < 2:
            return s
        i = 0 
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = 0 
            else:
                i += 1
        return s
    
        # solution 2: Time Limit Exceeded
        if len(s) < 2:
            return s
        lst_s = list(s)
        i = 0 
        while i < len(lst_s) - 1:
            if lst_s[i] == lst_s[i+1]:
                lst_s[i] = '#'
                lst_s[i+1] = '#'
                i += 2
            else:
                i += 1
        new_s = ''.join(lst_s).replace('##', '')
        if new_s == s:
            return new_s
        else:
            return self.removeDuplicates(new_s)
        
        
        # solution 1: Time Limit Exceeded
        if len(s) < 2:
            return s
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                new_s = s[:i] + s[i+2:]
                return self.removeDuplicates(new_s)
        else:
            return s
                
