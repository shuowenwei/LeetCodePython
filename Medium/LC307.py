# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/range-sum-query-mutable/

LC303, LC304, LC560, LC528
segment tree: refer to https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/Python%3A-Well-commented-solution-using-Segment-Trees
"""
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #helper function to create the tree from input array
        def createTree(nums, l, r):
            
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of all leaves under root
            #i.e. those elements lying between (start, end)
            root.total = root.left.total + root.right.total
                
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            
            return root.total
        
        return updateVal(self.root, index, val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeSum(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
            
        return rangeSum(self.root, left, right)
    
    
# My Solution: Time Limit Exceeded
class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[::]
        self.preSum = [0] * (len(nums) + 1)
        self.n = len(self.preSum)
        for i in range(1, self.n):
            self.preSum[i] = self.nums[i-1] + self.preSum[i-1]
        
    # Time Limit Exceeded
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        original_val = self.nums[index]
        diff = val - original_val
        self.nums[index] = val # need to update the value
        for i in range(index+1, self.n):
            self.preSum[i] += diff

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # need nums[left] + nums[left + 1] + ... + nums[right], inclusive of left and right
        return self.preSum[right+1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)