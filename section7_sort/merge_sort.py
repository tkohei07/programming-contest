import sys
sys.path.append('../')

from tools import input_output_tools

INFINITY = 2000000000


def merge(A, left, mid, right, count):
    left_num = mid - left
    right_num = right - mid
    L, R = [], []
    for i in range(left_num):
        L.append(A[left + i])
    for j in range(right_num):
        R.append(A[mid + j])
    L.append(INFINITY)
    R.append(INFINITY)
    i, j = 0, 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return count


def merge_sort(A, n, left_num, right_num, count):
    if left_num + 1 < right_num:
        mid_num = int((left_num + right_num) / 2)
        count = merge_sort(A, n, left_num, mid_num, count)
        count = merge_sort(A, n, mid_num, right_num, count)
        count = merge(A, left_num, mid_num, right_num, count)
    return count


if __name__ == "__main__":
    n, A = input_output_tools.input_two_line_numbers()
    count = 0
    count = merge_sort(A, n, 0, n, count)
    input_output_tools.output_list_as_numbers(A)
    print(count)
