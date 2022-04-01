"""
rh_users  = ["A", "B", "C", "X]
              |    |    |
              v    v    v
new_users = ["B", "C", "D", "Y"]

["A 3", "B 2", "C 1"], "X 1"]

A <- B <- C <- D
X <- Y 
    A
B       C
"""
import collections 
def solution(rh_users, new_users):
    all_users = set()
    dctDraph = collections.defaultdict(list)
    inDegree = collections.defaultdict(int)
    for user, referred_user in zip(rh_users, new_users):
        all_users.add(user)
        all_users.add(referred_user)
        dctDraph[referred_user].append(user)
        inDegree[user] += 1 # A, B, C, X 
        
    print(inDegree, dctDraph)
    leaderboard = collections.defaultdict(int)
    leafs = [user for user in all_users if inDegree[user] == 0]  # D, Y 
    q = collections.deque() 
    for l in leafs:
        q.append((l, 0))
        leaderboard[l] = 0
    while q: 
        cur_node, cur_score = q.popleft()
        leaderboard[cur_node] = cur_score
        print(leaderboard)
        for next_node in dctDraph[cur_node]:
            leaderboard[next_node] += leaderboard[cur_node] + 1
            inDegree[next_node] -= 1
            if inDegree[next_node] == 0:
                q.append((next_node, leaderboard[next_node]))

    score_name = [(score, name) for name, score in leaderboard.items()]
    score_name.sort(key = lambda x : (-x[0], x[1]))
    print(score_name)
    topThree = score_name[:3]
    return [namme + ' ' + str(score) for score, namme in topThree if score > 0]
        

def solution2(rh_users, new_users):
    all_users = set()
    dctDraph = collections.defaultdict(list)
    inDegree = collections.defaultdict(int)
    for user, referred_user in zip(rh_users, new_users):
        all_users.add(user)
        all_users.add(referred_user)
        dctDraph[referred_user].append(user)
        inDegree[user] += 1 # A, B, C, X 
        
    print(inDegree, dctDraph)
    leaderboard = collections.defaultdict(int)
    leafs = [user for user in all_users if inDegree[user] == 0] # D, Y 
    
    def dfs(node, score):
        leaderboard[node] = score
        for nei_node in dctDraph[node]:
            leaderboard[nei_node] += leaderboard[node] + 1
            inDegree[nei_node] -= 1
            if inDegree[nei_node] == 0:
                dfs(nei_node, leaderboard[nei_node])
    for l in leafs:
        dfs(l, 0)

    print(leaderboard)
    score_name = [(score, name) for name, score in leaderboard.items()]
    score_name.sort(key = lambda x : (-x[0], x[1]))
    topThree = score_name[:3]
    return [namme + ' ' + str(score) for score, namme in topThree if score > 0]


rh_users = ['A', 'B', 'C', 'X', 'X']
new_users = ['B', 'C', 'D', 'C2', 'C3']

rh_users = ['R', 'R', 'O', 'O', 'B', 'B']
new_users = ['O', 'B', 'C1', 'C2', 'C3', 'C4']
# print(solution(rh_users, new_users))
print(solution2(rh_users, new_users))

