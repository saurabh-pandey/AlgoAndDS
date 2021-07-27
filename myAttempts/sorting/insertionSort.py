def sort(arr):
  for i in range(1, len(arr)):
    data = arr[i]
    j = i
    while ( (arr[j-1] > data) and j > 0):
      arr[j] = arr[j-1]
      j -= 1
    arr[j] = data
