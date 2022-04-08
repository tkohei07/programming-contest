import sys
sys.path.append('../')
from bubble import bubble_sort
from selection_sort import selection_sort

bubble_count, bubble_sorted_numbers = bubble_sort(A, num)
selection_count, selection_sorted_numbers = selection_sort(A,num)

