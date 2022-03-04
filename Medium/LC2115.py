# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

LC797, LC207, LC210, LC2115
"""
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        res = []
        # supplies = set(supplies)
        dictRecipes = collections.defaultdict(set)   
        dictIndegree = collections.defaultdict(int)
        for rep, ing_list in zip(recipes, ingredients):
            dictIndegree[rep] = len(ing_list)
            for ing in ing_list:
                dictRecipes[ing].add(rep)
        
        starters = [s for s in supplies if dictIndegree[s] == 0] 
        q = collections.deque(starters)
        while q: 
            cur_node = q.popleft()
            for nei_node in dictRecipes[cur_node]:
                dictIndegree[nei_node] -= 1
                if dictIndegree[nei_node] == 0:
                    q.append(nei_node)
                    if nei_node in recipes:#and nei_node not in res:
                        res.append(nei_node)
        # print(res, dictIndegree)        
        return res 

        
                
            
                