logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]

logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]

import collections 
def getUserMaxMinAccessTime(logs):
    dctUser2Time = dict()
    for time, user, resource in logs:
        if user not in dctUser2Time:
            dctUser2Time[user] = [2**32, -2*32] # [min, max]
        dctUser2Time[user][0] = min(dctUser2Time[user][0], int(time))
        dctUser2Time[user][1] = max(dctUser2Time[user][1], int(time))
    return  dctUser2Time
# print(getUserMaxMinAccessTime(logs1))

def getHighestAccessedResource(logs):
    dctResource2Freq = collections.defaultdict(int)
    time2resource = [(int(time), resource) for time, user, resource in logs]
    time2resource.sort(key = lambda x: x[0])
    print(time2resource)
    left, right = 0, 0
    max_r = ''
    max_freq = 0
    while right < len(time2resource):
        while time2resource[right][0] - time2resource[left][0] <= 300:
            enter_r = time2resource[right][1]
            dctResource2Freq[enter_r] += 1
            # print('***', enter_r, dctResource2Freq)
            if dctResource2Freq[enter_r] > max_freq:
                max_freq = dctResource2Freq[enter_r]
                max_r = enter_r
            right += 1
            if right == len(time2resource):
                break
        exit_r = time2resource[left][1]
        dctResource2Freq[exit_r] -= 1
        left += 1
    return max_r, max_freq
print(getHighestAccessedResource(logs1))

def getTransitionGraph(logs):
    dctUser2TimeResource = collections.defaultdict(list)
    for time, user, resource in logs:
        dctUser2TimeResource[user].append((int(time), resource))

    dctResource2Next = collections.defaultdict(list)
    for user, time_resource in dctUser2TimeResource.items():
        time_resource.sort(key = lambda x: x[0])
        cur_resource = 'START'
        for i in range(len(time_resource)):
            next_resource = time_resource[i][1]
            dctResource2Next[cur_resource].append(next_resource)
            cur_resource = next_resource
        dctResource2Next[cur_resource].append('END')
    # print(dctResource2Next)
    
    dctGraph = collections.defaultdict(list)
    for key, lstResource in dctResource2Next.items():
        for r in set(lstResource):
            prob = lstResource.count(r) / float(len(lstResource))
            prob = round(prob, 3)
            dctGraph[key].append((r, prob))
    return dctGraph

print(getTransitionGraph(logs1))

"""
第二题：Resource Access Log
Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, 
the ID of the user making the access, and the resource ID.
The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.
For example:
logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]
Example 2:
logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]

Question 1 - Write a function that takes the logs and returns each users min and max access timestamp
Example Output:
user_3:[53760,53760]
user_2:[54060,62314]
user_1:[54001,58523]
user_7:[400,400]
user_6:[2,215]
user_5:[53651,53651]
user_4:[58522,58522]
user_8:[100,100]
*/

第二题FollowUp：
/*
Question 2 - Write a function that takes the logs and returns the resource with the highest number of accesses 
in any 5 minute window, together with how many accesses it saw.
Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3) 

Follow Up Question 3 -
Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency 
list with probabilities. Add START and END states. 
Specifically, for each resource, we want to compute a list of every possible next step taken by any user, 
together with the corresponding probabilities. The list of resources should include START but not END, 
since by definition END is a terminal state.

Expected output for logs1:
transition_graph(logs1) # =>
{{
'START': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},
'resource_1': {'resource_6': 0.333, 'END': 0.667},
'resource_2': {'END': 1.0},
'resource_3': {'END': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},
'resource_4': {'END': 1.0},
'resource_5': {'resource_4': 1.0},
'resource_6': {'END': 0.5, 'resource_5': 0.5}
}}
For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 
2 users have resource_1 as a first visit (user_6, user_22), 
1 user has resource_2 as a first visit (user_7), and 1 user has resource_6 (user_8) 
so the possible next steps for START are resource_3 with probability 4/8, resource_1 with probability 2/8, 
and resource_2 and resource_6 with probability 1/8.
These are the resource paths per user for the first logs example, ordered by access time:
{{
'user_1': ['resource_3', 'resource_3', 'resource_1'],
'user_2': ['resource_3', 'resource_2'],
'user_3': ['resource_3'],
'user_5': ['resource_3'],
'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'],
'user_7': ['resource_2'],
'user_8': ['resource_6'],
'user_22': ['resource_1'],
}}
Ex‍‍‍‍‌‌‍‌‍‍‍‌‌‍‍‍pected output for logs2:
transition_graph(logs2) # =>
{{
'START': {'resource_3': 1.0},
'resource_3': {'resource_3: 0.857, 'END': 0.143}
}
"""