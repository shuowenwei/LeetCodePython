# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reconstruct-itinerary/
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) == 1:
            return tickets[0]
        # all_cities = [t[0] for t in tickets] + [t[1] for t in tickets]
        # c = collections.Counter(all_cities)
        # for city, cnt in c.items():
        #     if cnt % 2 == 1 and city != 'JFK':
        #         destination = city
        import collections 
        map_dict = collections.defaultdict(list)
        for flight in tickets:
            map_dict[flight[0]] += flight[1],
        self.final_res = ["JFK"]
        
        def dfs_helper(flightfrom):
            destination_list = sorted(map_dict[flightfrom]) 
            for dstn in destination_list:
                map_dict[flightfrom].remove(dstn)
                self.final_res += dstn,
                dfs_helper(dstn)
                if len(self.final_res) == len(tickets) + 1:
                    return self.final_res
                self.final_res.pop()
                map_dict[flightfrom] += dstn,
        return dfs_helper('JFK')