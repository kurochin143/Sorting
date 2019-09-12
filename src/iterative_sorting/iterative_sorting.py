# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        cur_val = arr[i]
        for j in range(i + 1, len(arr)):
            sub_cur_val = arr[j]
            if sub_cur_val < cur_val:
                cur_val = sub_cur_val
                smallest_index = j

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr

# arr = [7,5,2,8,6]
# arr = selection_sort(arr)
# print(arr)

def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            i2 = i + 1
            if arr[i2] < arr[i]:
                swapped = True
                temp = arr[i]
                arr[i] = arr[i2]
                arr[i2] = temp

    return arr

# arr = [7,5,2,8,6]
# bubble_sort(arr)
# print(arr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0: return []

    if (maximum == -1):
        # find maximum value
        maximum = arr[0]
        for i in range(1, len(arr)):
            cur_val = arr[i]
            if (cur_val < 0): return "Error, negative numbers not allowed in Count Sort"
            if cur_val > maximum:
                maximum = cur_val

    # create a count array with range up to the max value in the arr
    count_arr = [0] * (maximum + 1)

    for v in arr:
        # increment count of the value
        count_arr[v] += 1

    # add count of current index to the next one
    for i in range(0, len(count_arr) - 1):
        count_arr[i + 1] += count_arr[i]

    out_arr = [0] * len(arr)

    for v in arr:
        out_arr[count_arr[v] - 1] = v # use count-1 as index for the value in out_arr
        count_arr[v] -= 1 # decrement count

    return out_arr

arr = [7,5,2,8,6,6]
arr = count_sort(arr)
print(arr)