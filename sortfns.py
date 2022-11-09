def counting_sort(arr):
  count = [0 for _ in range(999999)]

  for num in arr:
    count[num] += 1

  for i in range(1, len(count)):
    count[i] += count[i - 1]

  temp = [0 for _ in range(len(arr))]

  for num in arr:
    temp[count[num] - 1] = num
    count[num] -= 1

  for i in range(len(temp)):
    arr[i] = temp[i]

  return arr

def insertion_sort(arr):
  for i in range(len(arr)):
    if i % 1000 == 0:
      print(f'Insertion sort: {str(i)}/{str(len(arr))} ({i / len(arr)} %')
    j = i + 1
    if j >= len(arr) or arr[i] <= arr[j]:
      continue

    while j > 0 and arr[j] < arr[j - 1]:
      temp = arr[j]
      arr[j] = arr[j - 1]
      arr[j - 1] = temp
      j -= 1

  return arr

def selection_sort(arr):
  for i in range(len(arr)):
    if i % 1000 == 0:
      print(f'Selection sort: {str(i)}/{str(len(arr))} ({i / len(arr)} %')
    min_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

  return arr

# helper for quick_sort
def partition(arr, low, high):
  pivot = arr[high]
  insertion_point = low

  for j in range(low, high):
    if arr[j] <= pivot:
      temp = arr[insertion_point]
      arr[insertion_point] = arr[j]
      arr[j] = temp
      insertion_point += 1

  # swap pivot with insertion point
  temp = arr[insertion_point]
  arr[insertion_point] = arr[high]
  arr[high] = temp

  return insertion_point

def quick_sort(arr, low=0, high=None):
  if high is None:
    high = len(arr) - 1

  if low < high:
    pivot = partition(arr, low, high)
    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)

  return arr

# helper for merge_sort
def merge(arr1, arr2):
  i = 0
  j = 0
  merged = []

  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      merged.append(arr1[i])
      i += 1
    else:
      merged.append(arr2[j])
      j += 1

  while i < len(arr1):
    merged.append(arr1[i])
    i += 1

  while j < len(arr2):
    merged.append(arr2[j])
    j += 1

  return merged

def merge_sort(arr, left=0, right=None):
  if right is None:
    right = len(arr) - 1

  if left < right:
    mid = (left + right) // 2

    left_sorted = merge_sort(arr, left, mid)
    right_sorted = merge_sort(arr, mid + 1, right)

    return merge(left_sorted, right_sorted)

  return [arr[left]]

# helper for heap_sort
def heapify(arr, n, root):
  largest = root
  left_child = 2 * root + 1
  right_child = 2 * root + 2

  if left_child < n and arr[left_child] > arr[largest]:
    largest = left_child

  if right_child < n and arr[right_child] > arr[largest]:
    largest = right_child

  if largest != root:
    temp = arr[root]
    arr[root] = arr[largest]
    arr[largest] = temp

    heapify(arr, n, largest)

def heap_sort(arr):
  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  for i in range(n - 1, 0, -1):
    temp = arr[0]
    arr[0] = arr[i]
    arr[i] = temp

    heapify(arr, i, 0)

  return arr

def test(arr):
  arr[0] = 'THIS IS A TEST'
  return arr