# example: 4
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