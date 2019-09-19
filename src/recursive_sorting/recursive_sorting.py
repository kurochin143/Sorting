
def merge( arrA, arrB ):
    a_len = len(arrA)
    b_len = len(arrB)
    elements = a_len + b_len
    merged_arr = [0] * elements

    ai = 0 # current a index
    bi = 0 # current b index
    for i in range(elements):
        if ai == a_len: # a exhausted
            # insert remaining b
            for bii in range(bi, b_len):
                merged_arr[i] = arrB[bii]
                i += 1
            break
        elif bi == b_len: # b exhausted
            # insert remaining a
            for aii in range(ai, a_len):
                merged_arr[i] = arrA[aii]
                i += 1
            break
        else:
            a = arrA[ai]
            b = arrB[bi]
            if a < b:
                merged_arr[i] = a
                ai += 1
            else:
                merged_arr[i] = b
                bi += 1
    
    return merged_arr

def merge_sort( arr ):
    # split, merge, return
    arr_len = len(arr)
    if (arr_len > 1):
        mid = int((arr_len - 1) / 2)
        arrA = merge_sort([arr[i] for i in range(0, mid + 1)])
        arrB = merge_sort([arr[i] for i in range(mid + 1, arr_len)])
        return merge(arrA, arrB)

    return arr

arr = [8,6,5,9,1,-1,-100]
arr2 = merge_sort(arr)
print(arr2)

def merge_in_place(arr, start, mid, end):
    ri = mid + 1 # index of right array
    for i in range(start, ri):
        l = arr[i]
        r = arr[ri]
        if r < l:
            # swap
            arr[i] = r
            arr[ri] = l
            # single bubble sort
            for j in range(ri, end):
                c = arr[j]
                n = arr[j + 1]
                if c > n:
                    # move c to the right
                    # swap
                    arr[j] = n
                    arr[j + 1] = c
                else: # c is at the correct position
                    break

    return arr

# arr = [2,4,5,1,3]
# l = 0
# r = len(arr) - 1
# merge_in_place(arr, 0, int(l + (r - l) / 2), r)
# print(arr)

def merge_sort_in_place(arr, l, r): 
    # split, merge, return

    if l < r:
        mid = int(l + (r - l)/2)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid, r)
    
    return arr

# arr = [3,2]
# l = 0
# r = len(arr) - 1
# merge_sort_in_place(arr, l, r)
# print(arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        selected_index = i
        for j in range(i - 1, -1, -1):
            if arr[selected_index] < arr[j]:
                temp = arr[j]
                arr[j] = arr[selected_index]
                arr[selected_index] = temp
                selected_index = j
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):
    if len(arr) < 64:
        return insertion_sort(arr)
    else:
        return merge_sort_in_place(arr, 0, len(arr) - 1)

arr = [3,2,1,4,0]
print(timsort(arr))