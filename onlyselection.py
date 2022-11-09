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

start = time.time()
print_arr_to_file('outputs/selection_sort.txt', sortfns.selection_sort(nums))

runtime = time.time() - start
time_summary = ['Selection sort: ' + str(start) + ' s']
print_arr_to_file('outputs/selection_runtime.txt', time_summary)