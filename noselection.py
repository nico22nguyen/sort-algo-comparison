import os
import time
import sortfns

def read_ints_to_arr(filename):
  with open(filename) as f:
    lines = f.readlines()
    f.close()

    return [int(line) for line in lines]

def print_arr_to_file(filename, arr):
  slash_index = filename.rfind('/')
  if slash_index != -1:
    dirname = filename[:slash_index]
    if not os.path.exists(dirname):
      os.mkdir('./' + dirname)
  with open(filename, 'w') as f:
    for el in arr:
      f.write(str(el) + '\n')
    f.close()

nums = read_ints_to_arr('numbers.txt')
copies = [nums.copy() for _ in range(5)]
times = [0 for _ in range(5)]

counting_sort_start = time.time()
print_arr_to_file('outputs/counting_sort.txt', sortfns.counting_sort(copies[0]))
times[0] = time.time() - counting_sort_start

insertion_sort_start = time.time()
print_arr_to_file('outputs/insertion_sort.txt', sortfns.insertion_sort(copies[1]))
times[1] = time.time() - insertion_sort_start

quick_sort_start = time.time()
print_arr_to_file('outputs/quick_sort.txt', sortfns.quick_sort(copies[2]))
times[3] = time.time() - quick_sort_start

merge_sort_start = time.time()
print_arr_to_file('outputs/merge_sort.txt', sortfns.merge_sort(copies[3]))
times[4] = time.time() - merge_sort_start

heap_sort_start = time.time()
print_arr_to_file('outputs/heap_sort.txt', sortfns.heap_sort(copies[4]))
times[5] = time.time() - heap_sort_start

times_summary = [
  'Counting sort: ' + str(times[0]) + ' s',
  'Insertion sort: ' + str(times[1]) + ' s',
  'Selection sort: ' + str(times[2]) + ' s',
  'Quick sort: ' + str(times[3]) + ' s',
  'Merge sort: ' + str(times[4]) + ' s',
  'Heap sort: ' + str(times[5]) + ' s'
]
print_arr_to_file('outputs/times_summary.txt', times_summary)