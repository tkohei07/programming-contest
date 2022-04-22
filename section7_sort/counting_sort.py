import sys
sys.path.append('../')

from tools import input_output_tools


def counting_sort(A, n, k):
    B, C = [], []
    for _ in range(0, k):
        B.append(0), C.append(0)
    for j in range(0, n):
        C[A[j]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for j in range(1, n+1):
        num = A[j]
        B[C[num]] = num
        C[num] -= 1
    print(B[:n])


if __name__ == "__main__":
    VMAX = 10000
    n, A = input_output_tools.input_two_line_numbers()
    A = [0] + A
    counting_sort(A, n, VMAX)
