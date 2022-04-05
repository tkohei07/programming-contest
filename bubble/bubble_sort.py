import sys
sys.path.append('../')
from tools import input_output_tools

def bubble_sort(A, num):
	count = 0
	for i in range(num):
		for j in range(num-1, i, -1):
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
				count += 1

	return count, A

num, A = input_output_tools.input_two_line_numbers()
count, A = bubble_sort(A, num)

input_output_tools.output_list_as_numbers(A)
print(count)