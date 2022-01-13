# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/video-stitching/

https://labuladong.gitee.io/algo/3/27/104/

LC435, LC452, LC253, LC1024 - greedy
"""
class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        clips.sort(key=lambda x: x[0]) # // 按起点升序排列，起点相同的降序排列
        n = len(clips)
        res = 0 # // 记录选择的短视频个数
        curEnd, nextEnd = 0, 0 # cover 0 in [0, times]
        i = 0
        while i<n and clips[i][0] <= curEnd:
            # // 在第 res 个视频的区间内贪心选择下一个视频
            while i<n and clips[i][0] <= curEnd:
                nextEnd = max(nextEnd, clips[i][1])
                i += 1
            # // 找到下一个视频，更新 curEnd
            res += 1
            curEnd = nextEnd
            if nextEnd >= time: # // 已经可以拼出区间 [0, time]
                return res
        return -1 
        