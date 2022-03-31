import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def minOperations(arr):
  # Write your code here
  n = len(arr)
  target = ''.join([str(i) for i in sorted(arr)])
  cur = ''.join([str(i) for i in arr])
  import collections
  q = collections.deque()
  visited = set()
  q.append((cur, 0))
  visited.add(cur)
  while q:
    size = len(q)
    for i in range(size):
      cur, step = q.popleft()
      if cur == target:
        return step 
      for i in range(n):
        for j in range(n):
          new_state = cur[:i] + cur[i:j+1][::-1] + cur[j+1:]
          if new_state not in visited:
            q.append((new_state, step+1))
            visited.add(new_state)
  return -1 


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # Add your own test cases here
  