# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sort-an-array/

https://labuladong.github.io/algo/2/19/38/

#merge sort
LC912, LC179
"""
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        if l > r:
            return []
        if l == r:
            return [nums[l]]
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] > l2[j]:
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res
    
    # other solutions: 
    # https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap
class Solution:
    def sortArray(self, nums):
        # self.quickSort(nums)
        # self.mergeSort(nums)
        # self.bubbleSort(nums)
        # self.insertionSort(nums)
        # self.selectionSort(nums)
        self.heapSort(nums)
        return nums
    
    # @bubbleSort, TLE
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
    # @insertionSort, TLE
    def insertionSort(self, nums): 
        for i in range(1, len(nums)): 
            key = nums[i]
            j = i-1
            while j >= 0 and key < nums[j] : 
                    nums[j + 1] = nums[j] 
                    j -= 1
            nums[j + 1] = key
        
    # @selectionSort, TLE
    def selectionSort(self, nums):
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min
        return nums
    
    # @quickSort
    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail: return 
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
        return nums
     
    # @mergeSort
    def mergeSort(self, nums): 
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
   
   # @heapSort
    def heapSort(self, nums):
        def heapify(nums, n, i): 
            l = 2 * i + 1
            r = 2 * i + 2
            
            largest = i
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]: 
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0) 
Sort Objects:

[Pyhon]

class Node:
    def __init__(self, val):
        self.val = val

    def __cmp__(self, other):
        if self.val < other.val:
            return -1
        elif self.val > other.val:
            return 1
        else:
            return 0

class Solution(object):
    def sortArray(self, nums):
        nodes = [Node(n) for n in nums]
        return [node.val for node in sorted(nodes)]
[Pyhon3] notice, in python3, we don't have __cmp__(self, other) any more

class Node:
    def __init__(self, val):
        self.val = val
    
    # lt means less than, le means less or equal than etc.
    def __lt__(self, other):
        return self.val < other.val
    # incase you need more logic
    # def __le__(self, other):
    #     return self.val <= other.val
    # def __eq__(self, other):
    #     return self.val == other.val
    # def __ne__(self, other):
    #     return self.val != other.val
    # def __gt__(self, other):
    #     return self.val > other.val
    # def __ge__(self, other):
    #     return self.val >= other.val

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nodes = [Node(n) for n in nums]
        return [node.val for node in sorted(nodes)]