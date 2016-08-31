# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

solution reference link: https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution/2

the basic idea is, to permute n numbers, we can add the nth number into the resulting List<List<Integer>> from the n-1 numbers, in every possible position.

For example, if the input num[] is {1,2,3}: First, add 1 into the initial List<List<Integer>> (let's call it "answer").

Then, 2 can be added in front or after 1. So we have to copy the List<Integer> in answer (it's just {1}), add 2 in position 0 of {1}, then copy the original {1} again, and add 2 in position 1. Now we have an answer of {{2,1},{1,2}}. There are 2 lists in the current answer.

Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then copy {2,1} and {1,2}, and add 3 into position 1, then do the same thing for position 3. Finally we have 2*3=6 lists in answer, which is what we want.



"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]] 
        for n in nums: 
            new_perms = [] 
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append( perm[:i]+[n]+perm[i:] )
            perms = new_perms
        return perms 