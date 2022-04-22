import sys
sys.path.append('../')
from bubble import bubble_sort
from selection_sort import selection_sort

A = [4, 9, 4, 2, 3]
num = 5

# changing the value of A
bubble_count, bubble_sorted_numbers = bubble_sort.bubble_sort(A, num)
selection_count, selection_sorted_numbers = selection_sort.selection_sort(A, num)

print(bubble_sorted_numbers)
print(selection_sorted_numbers)