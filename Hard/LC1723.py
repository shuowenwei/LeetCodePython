# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1010057/JavaPython-Binary-Search-100

"""
class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        jobs.sort(reverse = True)
        res = [sum(jobs)]
        count = [0] * k 
        left, right  = max(jobs), max(jobs)
        def backtracking(index, jobs):
            if index == len(jobs):
                res[0] = min(res[0], max(count))
                return 
            for j in range(k):
                if count[j] + jobs[index] < res[0]:
                    count[j] += jobs[index]
                    backtracking(index + 1, jobs)
                    count[j] -= jobs[index]
                if count[j] == 0:
                    break 
        backtracking(0, jobs)
        return res[0]

        # backtracking + BS, faster
        jobs.sort(reverse = True)
        def backtracking(index, jobs, x):
            if index == len(jobs):
                return True 
            for j in range(k):
                if cap[j] >= jobs[index]:
                    cap[j] -= jobs[index]
                    if backtracking(index + 1, jobs, x):
                        return True
                    cap[j] += jobs[index]
                if cap[j] == x:
                    break 
            return False

        # binary search
        left, right = max(jobs), sum(jobs)
        while left < right:
            x = left + (right - left) / 2
            cap = [x] * k
            if backtracking(0, jobs, x):
                right = x
            else:
                left = x + 1
        return left