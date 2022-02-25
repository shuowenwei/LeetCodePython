# https://www.1point3acres.com/bbs/thread-855045-1-1.html
# n个服务员，m个人等位，给了数组里面元素是每个服务员服务一个人的时间，m>>n，当多个服务员空闲时候，
# 编号最小的去服务，问当你是第m+1个人的时候要等多久
# LC1071, 
from heapq import heappush, heappop
def getWaitingTime(nums, m):
    
    perpoleServed = []
    hp = []
    for index, time in enumerate(nums):
        heappush(hp, (index, time))
    while len(perpoleServed) < m: 
        pass 
    
    return res 

    
class Solution(object):
    def getOrder(self, tasks):
        tasks_index = [(t[0], t[1], index) for index, t in enumerate(tasks)]
        tasks_index.sort(key = lambda x: x[0])
        
        from heapq import heappush
        res = []
        hp = []
        process_index = 0 
        cur_time = tasks_index[process_index][0] # earliest task to enter queue 
        while len(res) < len(tasks_index): # break when all tasks are processed 
            # push all tasks with enter_time <= cur_time, when picking the shortest on to start
            while process_index < len(tasks_index) and tasks_index[process_index][0] <= cur_time:
                enter, processtime, index = tasks_index[process_index]
                heappush(hp, (processtime, index))
                process_index += 1
            if hp:
                processtime, index = heappop(hp)
                cur_time += processtime
                res.append(index)
            elif process_index < len(tasks_index):
                cur_time = tasks_index[process_index][0]
        return res 
    
def getPeopleServed(nums, x): # at time x
    res = 0
    for n in nums:
        res += int(x / n)
    return res 
nums = [2,4,3,2,3]
m = 20 
print(getPeopleServed(nums, 5))
print(getPeopleServed(nums, 6))