# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/strobogrammatic-number-iii/

https://www.youtube.com/watch?v=dK25e5q4p0Y
"""
class Solution(object):
    def strobogrammaticInRange(low, high):
        res = [0]
        
        def dfs(l ,r):
            pass 
        
        return res[0]        
        

def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = helper(n, n)
    return result


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        print(n, length)
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result

print("n = 2: \n",gen_strobogrammatic(2))
print("n = 3: \n",gen_strobogrammatic(3))
print("n = 4: \n",gen_strobogrammatic(4))
