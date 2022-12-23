from typing import List

def find_disappeared_numbers(arr: List[int]) -> List[int]:
    sz = len(arr)
    if sz < 2:
        return arr.copy()
  
    i = 0
    while i < sz:
        if (arr[i] != i + 1) and (arr[arr[i] - 1] != arr[i]):
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
        else:
            i += 1
  
    disappeared_nums = []
    for i, n in enumerate(arr):
        if n != i + 1:
            disappeared_nums.append(i + 1)
    return disappeared_nums

