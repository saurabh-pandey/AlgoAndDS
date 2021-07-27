def sort(arr):
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(arr) - 1):
      if (arr[i+1] < arr[i]):
        swapped = True
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
