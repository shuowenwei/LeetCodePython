# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/can-place-flowers/

LC849, LC605
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # my solution 1, refer to LC849
        # [0] 1    [0, 0] 2
        if 1 not in flowerbed:
            return (len(flowerbed)+1)/2 >= n 
        res = 0 
        # midZeros = []
        preZeros, postZeros = 0, 0
        first_1_flag = True
        zeros = 0 
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                zeros += 1
            else: 
                #flowerbed[i] == 1
                if first_1_flag:
                    preZeros = max(preZeros, zeros)
                    first_1_flag = False
                else:
                    # midZeros.append(zeros)
                    res += (zeros-1)/2
                zeros = 0
            postZeros = zeros
        # print(preZeros, midZeros, postZeros)
        res += preZeros/2 + postZeros/2 # + sum([(m-1)/2 for m in midZeros])
        return res >= n

        # solution 2: greedy~~~~~
        # https://leetcode.com/problems/can-place-flowers/discuss/1048610/Python-Simple-solution-using-counting
        res = 0 
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                res += 1
                flowerbed[i] = 1
        return res >= n 
    
        # solution 3: long and ugly
        if 1 not in flowerbed:
            return (len(flowerbed)+1)/2 >= n 
        res = 0
        for i in range(len(flowerbed) - 1):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                res += 1
            elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                res += 1
            elif i == len(flowerbed) - 2 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i+1] = 1
                res += 1
        return res >= n 