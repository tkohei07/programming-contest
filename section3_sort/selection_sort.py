import sys
sys.path.append('../')
from tools import input_output_tools

def selection_sort(A, num):
	count = 0
	for i in range(num):
		minj = i
		for j in range(i, num):
			if A[j] < A[minj]:
				minj = j
		if minj != i:
			A[i], A[minj] = A[minj], A[i]
			count += 1

	return count, A

# num, A = input_output_tools.input_two_line_numbers()
# count, A = selection_sort(A, num)

# input_output_tools.output_list_as_numbers(A)
# print(count)