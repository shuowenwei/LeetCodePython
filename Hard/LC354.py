# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/russian-doll-envelopes/

https://labuladong.gitee.io/algo/3/24/76/
LC300, LC354
"""
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        dp_table = [1]*n
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1])) # 对其高度 h 进行降序排序
        for i in range(n): 
            for j in range(i, n): 
                # Time Limit Exceeded	
                # if envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]:
                #     dp_table[j] = max(dp_table[j], 1 + dp_table[i])
                # 对于宽度 w 相同的数对，要对其高度 h 进行降序排序。因为两个宽度相同的信封不能相互包含的，逆序排序保证在 w 相同的数对中最多只选取一个。
                if envelopes[j][1] > envelopes[i][1]:
                    dp_table[j] = max(dp_table[j], 1 + dp_table[i])
        return res
envelopes = []
sol = Solution()
res = sol.maxEnvelopes(envelopes)
print(res)