import sys
sys.path.append('../')
from tools import input_output_tools

# I regret to inform you that this source code is wrong...

# Q = [[name1, num1], [name2, num2], ...]
Q = []
LINES, PROC_TIME, Q = input_multiple_lines()
MAX_LIST_NUM = 100005

def enqueue(x, head_index, tail_index):
	Q.append([Q[head_index-1][0], x])
	if tail_index + 1 == MAX_LIST_NUM:
		tail_index = 0
	else:
		tail_index += 1
	return tail_index

def dequeue(head_index):
	x = Q[head_index][1]
	if head_index + 1 == MAX_LIST_NUM:
		head_index = 0
	else:
		head_index += 1
	return x, head_index

head_index = 0
tail_index = LINES
total_time = 0

while head_index != tail_index:
	head_num, head_index = dequeue(head_index)
	c = min(PROC_TIME, head_num)
	Q[head_index-1][1] -= c
	total_time += c
	if Q[head_index-1][1] > 0:
		tail_index = enqueue(Q[head_index][1], head_index, tail_index)
	else:
		print(Q[head_index-1][0], total_time)