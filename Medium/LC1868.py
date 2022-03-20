# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

https://walkccc.me/LeetCode/problems/1868/

LC443, LC1868

Example 1:
Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
Output: [[6,6]]
Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].
"""
class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        ans = []
        i = 0  # encoded1's index
        j = 0  # encoded2's index

        while i < len(encoded1) and j < len(encoded2):
            mult = encoded1[i][0] * encoded2[j][0]
            minFreq = min(encoded1[i][1], encoded2[j][1])
            
            if ans and mult == ans[-1][0]:
                ans[-1][1] += minFreq
            else:
                ans.append([mult, minFreq])
                
            encoded1[i][1] -= minFreq
            encoded2[j][1] -= minFreq
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return ans

# Time: O(|\texttt{encoded1}| + |\texttt{encoded2}|)O(∣encoded1∣+∣encoded2∣)
# Space: O(|\texttt{encoded1}| + |\texttt{encoded2}|)O(∣encoded1∣+∣encoded2∣)
