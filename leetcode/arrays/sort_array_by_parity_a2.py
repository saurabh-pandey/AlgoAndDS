from typing import List

def sort_array_by_parity(arr: List[int]) -> List[int]:
    sz = len(arr)
    if sz < 2:
        return arr
    
    even_index = 0
    odd_index = sz - 1
    while even_index < odd_index:
        if arr[even_index] % 2 == 0:
            even_index += 1
        elif arr[odd_index] % 2 == 1:
            odd_index -= 1
        elif arr[even_index] % 2 == 1 and arr[odd_index] % 2 == 0:
            arr[even_index], arr[odd_index] = arr[odd_index], arr[even_index]
            even_index += 1
            odd_index -= 1
    return arr
