def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def getPivot(arr, start, end):
    return start

def partition(arr, start, end):
    i = start;
    pivot = getPivot(arr, start, end)
    for j in xrange(start, end):
        if (arr[j+1] <= arr[pivot]):
            swap(arr, i+1, j+1)
            i += 1
    swap(arr, pivot, i)
    return i

def quickSort(arr, start, end):
    if ((end - start + 1) < 2):
        return
    pos = partition(arr, start, end)
    quickSort(arr, start, pos - 1)
    quickSort(arr, pos + 1, end)

def sort(arr):
    quickSort(arr, 0, len(arr) - 1)
    
