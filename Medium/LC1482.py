# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686529/Java-Binary-Search-with-detailed-explanation.-Runtime%3A-O(nLog(maxdays))-100

"""
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        # This method is to find the number of bouquets that can be formed on a given day.
        def getNumBouquets(bloomDay, x, k):
            flowersCollected = 0 
            numBouquets = 0 
            for bd in bloomDay:
                if bd <= x:
                    # If the current flower can be taken with in days then increase the flower flowersCollected.
                    flowersCollected += 1
                else:
                    flowersCollected = 0
                # If the flowersCollected is same as the required flower per bookie, then increase the bouquets count;
                if flowersCollected == k: 
                    numBouquets += 1
                    flowersCollected = 0
            return numBouquets
            
        if m * k > len(bloomDay):
            return -1
        left = 1 
        right = max(bloomDay)
        while left <= right:
            mid = left + (right - left) / 2
            numBouquest = getNumBouquets(bloomDay, mid, k)
            if numBouquest > m: 
                right = mid - 1 
            elif numBouquest < m:
                left = mid + 1
            elif numBouquest == m:
                right = mid - 1 
        return left 
