import sys
sys.path.append('../')

from tools import input_output_tools
import partition_sort

# this has not been completed!!

def quick_sort(A, p, r):
    if p <r:
        q = partition_sort.partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, p + 1, r)


if __name__ == "__main__":
    n, q, A = input_output_tools.input_multiple_lines()
    quick_sort(A, 0, n)
    print(A)
