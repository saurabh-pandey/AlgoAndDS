from typing import List

def replace_elements(arr: List[int]) -> List[int]:
    if not arr:
        return arr
    
    max_elem_right = arr[-1]
    arr[-1] = -1
    for i in range(len(arr) - 2, -1, -1):
        curr_val = arr[i]
        arr[i] = max_elem_right
        if curr_val > max_elem_right:
            max_elem_right = curr_val
    return arr        
