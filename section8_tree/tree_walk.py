import sys
sys.path.append('../')

from tools import input_output_tools
import binary_tree


def pre_parse(T, pre_parse_list, u):
    if u == -1:
        return None
    pre_parse_list.append(u)
    pre_parse(T, pre_parse_list, T[u]['left'])
    pre_parse(T, pre_parse_list, T[u]['right'])


def in_parse(T, in_parse_list, u):
    if u == -1:
        return None
    in_parse(T, in_parse_list, T[u]['left'])
    in_parse_list.append(u)
    in_parse(T, in_parse_list, T[u]['right'])


def post_parse(T, post_parse_list, u):
    if u == -1:
        return None
    post_parse(T, post_parse_list, T[u]['left'])
    post_parse(T, post_parse_list, T[u]['right'])
    post_parse_list.append(u)


def print_for_tree_walk(pre_parse_list, in_parse_list, post_parse_list):
    print("Preorder")
    for i in range(len(pre_parse_list)):
        print(f" {pre_parse_list[i]}", end="")
    print("")
    print("Inorder")
    for i in range(len(in_parse_list)):
        print(f" {in_parse_list[i]}", end="")
    print("")
    print("Postorder")
    for i in range(len(post_parse_list)):
        print(f" {post_parse_list[i]}", end="")


if __name__ == "__main__":
    length, A = input_output_tools.input_mulitiple_line_numbers()
    T = binary_tree.set_nums(A, length)
    pre_parse_list = []
    in_parse_list = []
    post_parse_list = []
    for i in range(0, length):
        if T[i]['parent'] == -1:
            root = i
    pre_parse(T, pre_parse_list, root)
    in_parse(T, in_parse_list, root)
    post_parse(T, post_parse_list, root)
    print_for_tree_walk(pre_parse_list, in_parse_list, post_parse_list)