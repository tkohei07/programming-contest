import sys
sys.path.append('../')

from tools import input_output_tools


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == "__main__":
    n, A = input_output_tools.input_two_line_numbers()
    q = partition(A, 0, n - 1)
    A[q] = '[' + str(A[q]) + ']'
    input_output_tools.output_list_as_numbers(A)
