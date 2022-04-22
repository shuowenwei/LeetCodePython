
# stack to track index of B 

# stack is empty

# solution(“B1B2S”) -> “1B2S” or “B12S” (either is acceptable)
# O(n) - time
# O(n) - space
# solution one: 
# def solution(transactions):
#     transactions = list(transactions)
#     stack_index_B = [] # to store index of B
#     for index, char in enumerate(transactions):
#         if char == 'B':
#             stack_index_B.append(index)
#         if char == 'S':
#             if stack_index_B:
#                 stack_index_B.pop()
#             else:
#                 transactions[index] = ''
#     while stack_index_B: 
#         transactions[stack_index_B.pop()] = ''
        
#     return ''.join(transactions)

# solution two:
# O(n): time
# O(1): extra space
def solution(transactions):
    num_B = 0 
    res_no_extra_S = ''
    # the first pass: remmove extra 'S' 
    for char in transactions:
        if char == 'B':
            num_B += 1
        if char == 'S': 
            if num_B == 0:
                continue 
            else:
                num_B -= 1 
        res_no_extra_S += char
    
    res_no_extra_B = ''
    num_S = 0 
    for char in res_no_extra_S[::-1]:
        if char == 'S':
            num_S += 1
        if char == 'B': 
            if num_S == 0:
                continue 
            else:
                num_S -= 1 
        res_no_extra_B += char
    
    return res_no_extra_B[::-1]
