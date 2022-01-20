# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/multiply-strings/

https://labuladong.gitee.io/algo/4/32/134/

LC43, LC224, LC227, LC772
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # solution 1: neat but equally fast
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = len(num1), len(num2)
        res = [0]*(n1+n2)
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                mul = int(num1[i])*int(num2[j])
                # // 乘积在 res 对应的索引位置
                pos_higher = i+j
                pos_lower = i+j+1 # further
                tmp = mul + res[pos_lower]
                res[pos_lower] = tmp % 10
                res[pos_higher] += tmp / 10
        return str(int(''.join([str(r) for r in res])))
        

        # my long and ugly solutiono:
        if num1 == '0' or num2 == '0':
            return '0'

        def compute(num1, digit, numOfZero):
            res = '0'*numOfZero
            # tmp = int(num1)*int(digit)
            # return str(tmp)+res
            carry = 0 
            for i in range(len(num1)-1, -1, -1):
                tmp = int(num1[i])*int(digit) + carry
                carry = tmp / 10
                res = str(tmp%10) + res
            if carry > 0:
                res = str(carry) + res
            return res 
        
        def addTwoNumber(s1, s2):
            if s1 == '0':
                return s2
            # alwasy make s1 longer
            if len(s1) < len(s2):
                s1, s2 = s2, s1 
            p1, p2 = len(s1)-1, len(s2)-1
            res = ''
            carry = 0
            while p1 >= 0 and p2 >= 0:
                tmp = int(s1[p1]) + int(s2[p2]) + carry
                carry = tmp / 10
                res = str(tmp%10) + res
                p1 -= 1
                p2 -= 1
            # print(s1, s2, p1, p2)
            if p1 >= 0:
                for k in range(p1, -1, -1):
                    tmp = int(s1[k]) + carry
                    carry = tmp / 10
                    res = str(tmp%10) + res
            if carry > 0:
                res = str(carry) + res
            # print('...', res)
            return res
        
        # alwasy make num1 longer
        if len(num1) < len(num2):
            num1, num2 = num2, num1 
        res = '0'
        for i in range(len(num2)-1, -1, -1):
            r = compute(num1, num2[i], len(num2)-1-i)
            # print(num1, num2[i], len(num2)-1-i, r)
            res = addTwoNumber(res, r)
        return res 
