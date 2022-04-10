import sys
sys.path.append('../')
from tools import input_output_tools

# example: A = [[5], [1, 2, 3, 4, 5], [3], [3, 4, 1]]
A = input_output_tools.input_four_lines()
n = A[0][0]
S = A[1]
S.append(0)
q = A[2][0]
T = A[3]
sum = 0

def linear_search_from_S(key, n):
	S[n] = key
	i = 0
	while S[i] != key:
		i += 1
	return i != n

for i in range(len(T)):
	key = T[i]
	if linear_search_from_S(T[i], n):
		sum += 1

print(sum)