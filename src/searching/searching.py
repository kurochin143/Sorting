# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if arr[i] == target: return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  low = 0
  high = len(arr)-1
  mid = int((low + high) / 2)

  while True:
    if target == arr[mid]: return mid
    elif target < arr[mid]:
      high = mid - 1
    else:
      low = mid + 1

    if low == high: 
      if arr[low] == target:
        return low
      else:
        return -1 # not found

    mid = int((low + high) / 2)

  return -1 # not found

#print(binary_search([0,1,2,3,4,5], 4))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

  if len(arr) == 0: return - 1
  
  middle = int((low + high) / 2)

  if target == arr[middle]: return middle
  elif target < arr[middle]:
    high = middle - 1
  else:
    low = middle + 1

  if low == high: 
    if arr[low] == target:
      return low
    else:
      return -1 # not found

  return binary_search_recursive(arr, target, low, high)

#print(binary_search_recursive([0,1,2,3,4,5,6], 4, 0, 7))