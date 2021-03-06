import sys

# input example: 4
#          3 2 6 9 
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

# example: 
# 3
# D 3
# H 2
# D 1
def input_multiple_lines():
    input_list = []
    # [lines q, name1 num1, name2 num2, ...]
    for l in sys.stdin:
        input_list.append(l)
    if ' ' in input_list[0]:
        lines, q = map(str, input_list[0].split())
    else:
        lines = input_list[0]
        q = '0'
    list_in_list = []
    # [[name1, num1], [name2, num2], ...]
    for i in range(1, len(input_list)):
        T = input_list[i].strip("\n").split()
        if q == '0':
            list_in_list.append([T[0], T[1]])
        else:
            list_in_list.append([T[0], int(T[1])])
    return int(lines), int(q), list_in_list

# 13
# 0 3 1 4 10
# 1 2 2 3
# 2 0
# 3 0
# 4 3 5 6 7
# 5 0
# 6 0
# 7 2 8 9
# 8 0
# 9 0
# 10 2 11 12
# 11 0
# 12 0
def input_mulitiple_line_numbers():
    input_list = []
    # [num, num1 num1' num1'' ... , num2 num2' num2'', ...]
    for l in sys.stdin:
        input_list.append(l)
    line_num = int(input_list[0])
    list_in_list = []
    # [[num1, num1', num1'', ...], [num2, num2', num2'', ...], ...]
    for i in range(1, len(input_list)):
        digit_list = list(map(int, input_list[i].split()))
        list_in_list.append(digit_list)
    return line_num, list_in_list


def input_four_lines():
    line_num = 4
    input_list = []
    for l in range(line_num):
        input_list.append(list(map(int, input().split())))
    return input_list


# for test
if __name__ == "__main__":
    print(input_multiple_lines())
