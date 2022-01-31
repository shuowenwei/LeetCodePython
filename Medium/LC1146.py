# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/snapshot-array/

"""
class SnapshotArray(object):
    
    def __init__(self, length):
        """
        :type length: int
        """
        self.snpa_id = 0
        self.snap_cache = []
        self.d = dict()
        
    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.d[index] = val
        
    def snap(self):
        """
        :rtype: int
        """
        self.snpa_id += 1
        self.snap_cache.append(dict(self.d))
        return self.snpa_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        dd = self.snap_cache[snap_id]
        if index in dd:
            return dd[index]
        else:
            return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
