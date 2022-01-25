# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-the-duplicate-number/

https://leetcode.com/problems/find-the-duplicate-number/discuss/72852/Python-same-solution-as-142-Linked-List-Cycle-II
https://leetcode.com/problems/find-the-duplicate-number/discuss/515872/Python-O(1)-aux-space-by-hopping.-83%2B-w-Hint

https://www.1point3acres.com/bbs/thread-841626-1-1.html

LC142, LC287
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = finder = 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    slow = nums[slow]
                    finder = nums[finder]
                return finder


        # another way of writing it:
        slow = fast = 0
        finder = 0 
        while True:
            # slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
                
        # Locate the start node of cycle (i.e., the duplicate number)
        while True:
            if finder != slow:
                slow = nums[slow]
                finder = nums[finder]
            if slow == finder:
                break
                
        return finder