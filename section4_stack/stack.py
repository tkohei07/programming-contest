import sys
sys.path.append('../')
from tools import input_output_tools

input_string_list = input_output_tools.input_operand_numbers()
S = []
top_index = 0

def push(num, top_index):
	S.append(num)
	top_index += 1

def pop(top_index):
	top_index -= 1
	tmp = S[top_index]
	del S[top_index]
	return tmp

for i in range(len(input_string_list)):
	factor = input_string_list[i]
	if factor == '+':
		a, b = pop(top_index), pop(top_index)
		push(a + b, top_index)
	elif factor == '-':
		a, b = pop(top_index), pop(top_index)
		push(b - a, top_index)
	elif factor == '*':
		a, b = pop(top_index), pop(top_index)
		push(a * b, top_index)
	else:
		push(int(factor), top_index)

print(S[0])