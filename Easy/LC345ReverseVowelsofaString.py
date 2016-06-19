
# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-vowels-of-a-string/

"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=0:
            return s
        vowels= 'aeiouAEIOU' 
        s_list = list(s)
        p = 0
        q = len(s_list)-1
        temp = ''
        while p < q:
            while p < q and s_list[p] not in vowels:
                p = p + 1
            while  p < q and s_list[q] not in vowels:
                q = q - 1
            if p < q:    
                temp = s_list[p]
                s_list[p] = s_list[q]
                s_list[q] = temp
                p = p + 1
                q = q - 1
        return ''.join(s_list) 
        
