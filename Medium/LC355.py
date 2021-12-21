# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/design-twitter/

https://labuladong.gitee.io/algo/2/20/47/

LC355 
"""
class User(object):
    def __init__(self, userId):
        self.userId = userId
        self.tweets = {}
        self.follows = set() # set of element:User
        self.followers = set() # set of element:User

from heapq import *
class Twitter(object):
    def __init__(self):
        self.users = dict()
        self.time = 0
        
    def create(self, userid):
        if userid not in self.users:
            self.users[userid] = User(userid)
            # the User must follow itself 
            self.users[userid].follows.add(self.users[userid])
            self.users[userid].followers.add(self.users[userid])

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.create(userId)
        self.users[userId].tweets[tweetId] = self.time
        self.time += 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        
        

    def follow(self, followerId, followeeId): # followeeId is the person being followed by some follower 
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.create(followerId)
        self.create(followeeId)
        self.users[followerId].follows.add(self.users[followeeId])
        self.users[followeeId].followers.add(self.users[followerId])
        
    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.create(followerId)
        self.create(followeeId)        
        if self.users[followerId] in self.users[followeeId].followers:
            self.users[followeeId].followers.remove(self.users[followerId])
            self.users[followerId].follows.remove(self.users[followeeId])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
