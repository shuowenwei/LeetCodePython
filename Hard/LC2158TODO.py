# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/amount-of-new-area-painted-each-day/

G: froom https://www.1point3acres.com/bbs/thread-889468-1-1.html

https://walkccc.me/LeetCode/problems/2158/

"""
from sortedcontainers import SortedList


class Solution:
  def amountPainted(self, paint: List[List[int]]) -> List[int]:
    minDay = min(s for s, e in paint)
    maxDay = max(e for s, e in paint)
    ans = [0] * len(paint)
    # store indices of paint that are available now
    runningIndices = SortedList()
    events = []  # (day, index, type)

    for i, (start, end) in enumerate(paint):
      events.append((start, i, 1))  # 1 := entering
      events.append((end, i, -1))  # -1 := leaving

    events.sort()

    i = 0  # events' index
    for day in range(minDay, maxDay):
      while i < len(events) and events[i][0] == day:
        day, index, type = events[i]
        if type == 1:
          runningIndices.add(index)
        else:
          runningIndices.remove(index)
        i += 1
      if runningIndices:
        ans[runningIndices[0]] += 1

    return ans
