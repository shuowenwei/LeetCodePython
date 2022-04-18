# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-of-smaller-numbers-after-self/

https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/445769/merge-sort-CLEAR-simple-EXPLANATION-with-EXAMPLES-O(n-lg-n)

find python version in the comments 

# merge sort
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[(num, i) for i,num in enumerate(nums)] # array with indexes, (num, index) tuples
        res=[0]*len(nums)
        
        def merge(left, right):
            l=0
            r=0
            out=[]
            numElemsRightArrayLessThanLeftArray=0
            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    out.append(right[r])
                    r += 1
                    numElemsRightArrayLessThanLeftArray += 1                 
                else:
                    out.append(left[l])
                    res[left[l][1]] += numElemsRightArrayLessThanLeftArray
                    l += 1
            if l < (len(left)):
                for i in range(l, len(left)):
                    out.append(left[i])
                    res[left[i][1]] += numElemsRightArrayLessThanLeftArray
            if r < (len(right)):
                for i in range(r,len(right)):
                    out.append(right[i])
            return out

        def merge_sort(arr):
            if len(arr)==1:
                return arr
            midIndex=len(arr)//2
            left_side=merge_sort(arr[:midIndex])
            right_side=merge_sort(arr[midIndex:])
            return merge(left_side, right_side)
        
        _ = merge_sort(arr)
        return res
