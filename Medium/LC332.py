# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reconstruct-itinerary/

"""
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if len(tickets) == 1:
            return tickets[0]
        # all_cities = [t[0] for t in tickets] + [t[1] for t in tickets]
        # c = collections.Counter(all_cities)
        # for city, cnt in c.items():
        #     if cnt % 2 == 1 and city != 'JFK':
        #         destination = city
        import collections 
        dctFrom2To = collections.defaultdict(list)
        for _from, _to in tickets:
            dctFrom2To[_from].append(_to)
            
        self.res = ["JFK"]
        def dfs_helper(flightfrom):
            
            destination_list = sorted(dctFrom2To[flightfrom]) 
            for dstn in destination_list:
                dctFrom2To[flightfrom].remove(dstn)
                self.res.append(dstn)
                dfs_helper(dstn)
                if len(self.res) == len(tickets) + 1:
                    return self.res
                self.res.pop()
                dctFrom2To[flightfrom].append(dstn)
        dfs_helper('JFK')
        return self.res
    
        # solution 2: - restructure via backtracking
        if len(tickets) == 1:
            return tickets[0]
        
        import collections 
        dctFrom2To = collections.defaultdict(list)
        for _from, _to in tickets:
            dctFrom2To[_from].append(_to)

        res = ['JFK']
        def backtracking(res):
            
            flightfrom = res[-1]
            destination_list = sorted(dctFrom2To[flightfrom])
            for dstn in destination_list:
                res.append(dstn)
                dctFrom2To[flightfrom].remove(dstn)
                backtracking(res)
                if len(res) == len(tickets) + 1:
                    return 
                res.pop()
                dctFrom2To[flightfrom].append(dstn)
                
        backtracking(res)      
        return res