from functools import lru_cache

import sys
sys.path.append('../')
from tools import input_output_tools

# @lru_cache()
def solve(i, m, A):
	if m == 0:
		return True
	if i >= n:
		return False
	res = solve(i + 1, m, A) or solve(i + 1, m - A[i], A)
	return res


if __name__ == "__main__":
	input_list = input_output_tools.input_four_lines()
	n = input_list[0][0]
	A = input_list[1]
	q = input_list[2][0]
	M = input_list[3]

	for m in M:
		if solve(0, m, A):
			print("yes")
		else:
			print("no")