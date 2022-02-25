# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/employee-importance/

"""
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        dict_id2employee = {}
        for em in employees:
            dict_id2employee[em.id] = em
        
        res = 0 
        q = collections.deque()
        q.append(dict_id2employee[id])
        while q:
            size = len(q)
            for i in range(size):
                cur_em = q.popleft()
                res += cur_em.importance
                if cur_em.subordinates:
                    for sub_id in cur_em.subordinates:
                        q.append(dict_id2employee[sub_id])
        return res 
                
            
