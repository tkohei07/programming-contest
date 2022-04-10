import sys
sys.path.append('../')
from tools import input_output_tools

# example: A = [[5], [1, 2, 3, 4, 5], [3], [3, 4, 1]]
A = input_output_tools.input_four_lines()
S = A[1]
q = A[2][0]
T = A[3]
sum = 0

def binary_search(key):
	right_index = A[0][0]
	left_index = 0
	while left_index < right_index:
		mid = int((left_index + right_index) / 2)
		if S[mid] == key:
			return True
		elif key < S[mid]:
			right_index = mid
		else:
			left_index = mid + 1
	return False

for i in range(q):
	key = T[i]
	if binary_search(T[i]):
		sum += 1

print(sum)