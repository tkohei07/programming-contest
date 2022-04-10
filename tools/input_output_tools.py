import sys

# input example: 4
#          3, 2, 6, 9 
def input_two_line_numbers():
    for i in range(2):
        if i == 0:
            num = int(input())
        else:
            digit = input()
            digit_list = list(map(int, digit.split()))
    return num, digit_list

def output_list_as_numbers(A):
    print(' '.join(map(str, A)))

# input example: 1 2 + 3 4 - *
def input_operand_numbers():
    input_string_list = list(input().split())
    return input_string_list

def input_multiple_lines():
    input_list = []
    # [lines q, name1 num1, name2 num2, ...]
    for l in sys.stdin:
        input_list.append(l)
    lines, q = map(str, input_list[0].split())
    list_in_list = []
    # [[name1, num1], [name2, num2], ...]
    for i in range(1, len(input_list)):
        T = input_list[i].strip("\n").split()
        list_in_list.append([T[0], int(T[1])])
    return int(lines), int(q), list_in_list

def input_four_lines():
    line_num = 4
    input_list = []
    for l in range(line_num):
        input_list.append(list(map(int, input().split())))
    return input_list