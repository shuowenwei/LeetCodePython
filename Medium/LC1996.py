# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1759517/C%2B%2B-oror-Python-oror-Comparator-Sorting-oror-Explained

LC300, LC354, LC1996 
"""
class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        # Sort by attack in increasing order and by defence in decreasing order.
        # Now travel from last idx and maintain max, if defence of this is less than max add it to ans.
        # In case of tie in attacks and max defence is of same attack, it wont be considered as we sorted defence in decreasing order.
        n = len(properties)
        properties.sort(key =lambda x:(x[0], -x[1]))
        res = 0
        max_defence = -sys.maxsize
        for i in range(n-1, -1, -1):
            defence = properties[i][1]
            if defence < max_defence:
                res += 1
            max_defence = max(max_defence, defence)
        return res


        # solution 2: 
        # refer to https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1841336/Find-strong-people-instead-of-weak-ones%3A-concise-python-solution-using-sort
	    # defense needs to be sorted reversely so 
		# at same attack level, weaker one will be examined first
        properties.sort(key=lambda x: (x[0], -x[1]))
        curr_max_dfe = properties[-1][1]
        strongs = 1
        for i in reversed(range(len(properties) - 1)):
			# if current defense >= max defence we examined, this one must be strong
            if properties[i][1] >= curr_max_dfe:
                strongs += 1
                curr_max_dfe = properties[i][1]
        return len(properties) - strongs