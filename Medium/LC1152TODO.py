# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/analyze-user-website-visit-pattern/

"""
import collections

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

def mostVisitedPattern(username, timestamp, website):
    dictUsertoWeb = collections.defaultdict(list)
    for user, time, web in zip(username, timestamp, website):
        dictUsertoWeb[user].append(web)
        
    def backtracking(websites, index, path, res, l = 3):
        if index == len(websites):
            if len(path) == l:
                res.append(path[::])
            return
        for i in range(index, len(websites)):
            path.append(websites[i])
            backtracking(websites, i + 1, path, res, l = 3)
            path.pop()
        
    dict_combs2count = collections.defaultdict(int)
    for user, webs in dictUsertoWeb.items():
        res = []
        backtracking(webs, 0, [], res, l = 3)
        for combs in res:
            dict_combs2count['-'.join(combs)] += 1
    print(dict_combs2count)

mostVisitedPattern(username, timestamp, website)

# Another solution: https://www.tutorialcup.com/leetcode-solutions/analyze-user-website-visit-pattern-leetcode-solution.htm
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        dic = defaultdict(list)
        for i in range(len(username)):
            dic[username[i]].append((website[i], timestamp[i]))
        for k, v in dic.items():
            v.sort(key=lambda x: x[1])
            new_v = []
            for web, time in v:
                new_v.append(web)
            dic[k] = new_v
            # print(k, new_v)

        combs = defaultdict(list)
        for k, v in dic.items():
            self.get_all_combinations(v, combs, [], 0, k)
        max_size = -1
        for k, v in combs.items():
            # print(k,v,'--------')
            max_size = max(max_size, len(v))
        max_list = []
        for k, v in combs.items():
            if len(v) == max_size and (not max_list or list(k) < max_list):
                max_list = list(k)
        return max_list
        
    def get_all_combinations(self, website, combs, comb, start, user):
        if user in combs[tuple(comb)]:
            return
        if len(comb) == 3:
            combs[tuple(comb)].append(user)
            return
        for i in range(start, len(website)):
            comb.append(website[i])
            self.get_all_combinations(website, combs, comb, i+1, user)
            comb.pop()
    
sol = Solution()
res = sol.mostVisitedPattern(username, timestamp, website)
print('solution 2 res', res)


# def backtracking(websites, index, path, res, l = 3):
#     if index == len(websites):
#         print(path)
#         if len(path) == l:
#             res.append(path[::])
#         return
#     for i in range(index, len(websites)):
#         path.append(websites[i])
#         backtracking(websites, i + 1, path, res, l = 3)
#         path.pop()
# webs = ['home', 'cart', 'maps', 'home']
# backtracking(webs, 0, [], res, l = 3)


just do 3 for loops: https://www.youtube.com/watch?v=V510Lbtrm5s