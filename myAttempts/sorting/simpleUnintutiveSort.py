# Based on this paper https://arxiv.org/abs/2110.01111
# Link to PDF: https://arxiv.org/pdf/2110.01111.pdf

def sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i] < arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp