# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/course-schedule-iii/

https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation

LC1834, LC630
greedy
LC207, LC210, LC630
"""
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        hp = []
        start = 0 
        courses.sort(key = lambda x: x[1])
        for time, endTime in courses:
            start += time
            heappush(hp, -time) # hp is courses taken 
            if start > endTime:
                lastLongestCourse = - heappop(hp)
                start -= lastLongestCourse
        return len(hp)
    
