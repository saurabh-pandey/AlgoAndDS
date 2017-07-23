def sort(arr):
    for i in xrange(len(arr) - 1):
        min = i
        for j in xrange(i+1, len(arr)):
            if (arr[j] <= arr[min]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
