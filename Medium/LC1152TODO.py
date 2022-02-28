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