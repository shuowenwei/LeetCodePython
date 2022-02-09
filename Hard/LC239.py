# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sliding-window-maximum/submissions/

solution: https://leetcode.com/problems/sliding-window-maximum/discuss/65901/9-lines-Ruby-11-lines-Python-O(n)
Keep indexes of good candidates in deque d. The indexes in d are from the current window, 
they're increasing, and their corresponding nums are decreasing. Then the first deque element is 
the index of the largest window value.

For each index i:

Pop (from the end) indexes of smaller elements (they'll be useless).
Append the current index.
Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
If our window has reached size k, append the current window maximum to the output.


solution: https://leetcode.com/problems/sliding-window-maximum/discuss/111560/Python-O(n)-solution-using-deque-with-comments

https://labuladong.gitee.io/algo/2/20/52/

LC239, LC480
"""
class MonotonicQueue(object):
    def __init__(self): 
        import collections
        self.q = collections.deque([])
    def push(self, num):
        while len(self.q) > 0 and self.q[-1] < num:
            self.q.pop()
        self.q.append(num)
    def max(self):
        return self.q[0]
    def pop(self, num):
        if num == self.q[0]: 
            self.q.popleft()
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        window = MonotonicQueue()
        for i in range(n):
            if i < k-1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k+1])
        return res 
        """
        d = collections.deque() 
        res = [] 
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n: 
                d.pop()

            d.append(i)
            if d[0] == i - k: 
                d.popleft()
            if i >= k - 1: 
                res.append(nums[d[0]])
        return res 
        """
            
        """
        from collections import deque 
        if not nums:
            return [] 
        if k == 0:
            return nums   
        
        res = []
        deq = deque()
        for i in range(k):
            while len(deq) != 0: 
                if nums[i] > nums[deq[-1]]:
                # found a index whose value is greater than current deq[-1], pop
                    deq.pop()
                else:
                    break
            deq.append(i) # 1st loop: get the index of the largest value in nums[:k]
        for i in range(k,len(nums)):
            res.append(nums[deq[0]])
            if deq[0] < i - k + 1:
                deq.popleft()
            while len(deq) != 0: 
                if nums[i] > nums[deq[-1]]: 
                    deq.pop()
                else:
                    break 
            deq.append(i)
        # add value from the last sequence 
        res.append(nums[deq[0]])
        return res 
        """

    
        # original solution: slow ... 
        """
        if len(nums) == 0 or k == 0:
            return []
        
        curMax = max(nums[:k])
        res = [curMax]
        for i in range(k,len(nums)):
            if nums[i] > curMax: 
                curMax = nums[i]
            res.append(curMax)
        return res 
        """