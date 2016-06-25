# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-binary/

"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = ''
        s = '' 
        if len(a) >= len(b):
            l,s = a,b
        else:
            l,s = b,a
        len_l = len(l)-1
        len_s = len(s)-1 
        res = ['0']*(max(len(a),len(b))+1)
        #print(res)
        carry = '0'
        while len_s >= 0:
            res[len_l+1] = str( (int(l[len_l])+int(s[len_s])+int(carry))%2 )
            #print(res)
            carry = str( (int(l[len_l])+int(s[len_s])+int(carry))/2 )
            len_l -= 1
            len_s -= 1
        while len_l >= 0:
            res[len_l+1] = str( (int(l[len_l])+int(carry))%2 )
            carry = str( (int(l[len_l])+int(carry))/2 )
            len_l -= 1
        res[0] = carry 
        res_str = ''.join(res)
        if res_str[0]=='0':
            return res_str[1:]
        else:
            return res_str
