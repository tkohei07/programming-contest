import sys
sys.path.append('../')

from tools import input_output_tools


def set_nums(A, length):
    T = []
    line = 0
    for i in range(length):
        T.append({'parent': -1, 'left': -1, 'right': -1})
    for i in range(length):
        v = A[i][0]
        d = A[i][1]
        for j in range(d):
            c = A[i][j+2]
            if j == 0:
                T[v]['left'] = c
            else:
                T[line]['right'] = c
            line = c
            T[c]['parent'] = v
    return T


def set_depth(T, D, u, p):
    D[u] = p
    if T[u]['right'] != -1:
        set_depth(T, D, T[u]['right'], p)
    if T[u]['left'] != -1:
        set_depth(T, D, T[u]['left'], p+1)
    return D


def print_one_line(i, T, D, A):
    print(f"node {i}: parent = {T[i]['parent']}, depth = {D[i]}, ", end='')
    if T[i]['parent'] == -1:
        print(f"root, {A[i][2:]}")
    elif T[i]["left"] == -1:
        print("leaf, []")
    else:
        print(f"internal node, {A[i][2:]}")


if __name__ == "__main__":
    length, A = input_output_tools.input_mulitiple_line_numbers()
    T = set_nums(A, length)
    D = [i for i in range(length)]
    r = 0
    for i in range(0, length):
        if T[i]['parent'] == -1:
            r = i
    D = set_depth(T, D, r, 0)
    for i in range(length):
        print_one_line(i, T, D, A)
