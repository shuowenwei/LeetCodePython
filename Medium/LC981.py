# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/time-based-key-value-store/

https://leetcode.com/problems/time-based-key-value-store/discuss/1643667/Python%3A-Using-Dict-and-Binary-Search

"""
class TimeMap(object):
    
    def __init__(self):
        self.dict_key = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.dict_key:
            self.dict_key[key] = [ (value, timestamp) ]
        else:
            self.dict_key[key].append( (value, timestamp) ) # increasing by timestampe
            
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.dict_key:
            return ''
        elif self.dict_key[key][0][1] > timestamp:
                return ''
        elif self.dict_key[key][-1][1] <= timestamp:
            return self.dict_key[key][-1][0]
        else:
            nums = self.dict_key[key]
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid][1] <= timestamp and nums[mid+1][1] > timestamp:
                    return nums[mid][0]
                elif nums[mid][1] < timestamp:
                    left = mid + 1
                elif nums[mid][1] > timestamp:
                    right = mid - 1
            return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
