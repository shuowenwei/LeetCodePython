# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/strobogrammatic-number-iii/

https://www.youtube.com/watch?v=dK25e5q4p0Y
"""
class Solution(object):
    def strobogrammaticInRange(low, high):
        res = [0]
    
        def helper(n):
            pairs = [('0','0'), ('1','1'), ('8','8'), ('6','9'), ('9','6')]
            if n == 0:
                return ''
            if n == 1:
                return ['0', '1', '8']
            
            cur_nums = []
            pre_nums = helper(n - 2)
            for pre in pre_nums:
                for front, back in pairs:
                    cur_nums.append(front + pre + back)
            for num in cur_nums:
                if (num == '0' or num[0] != '0') and len(low) <= len(num) <= len(high):
                    res[0] += 1
            
        helper(len(high))
        helper(len(high)-1)
        return res[0]        
        



# def gen_strobogrammatic(n):
#     """
#     :type n: int
#     :rtype: List[str]
#     """
#     result = helper(n, n)
#     return result

# def helper(n, length):
#     if n == 0:
#         return [""]
#     if n == 1:
#         return ["1", "0", "8"]
#     middles = helper(n-2, length)
#     result = []
#     for middle in middles:
#         print(n, length)
#         if n != length:
#             result.append("0" + middle + "0")
#         result.append("8" + middle + "8")
#         result.append("1" + middle + "1")
#         result.append("9" + middle + "6")
#         result.append("6" + middle + "9")
#     return result

# print("n = 2: \n",gen_strobogrammatic(2))
# print("n = 3: \n",gen_strobogrammatic(3))
# print("n = 4: \n",gen_strobogrammatic(4))
