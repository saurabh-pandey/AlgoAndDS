from typing import List

def valid_mountain_array(arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    is_increasing = True
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            return False
        elif arr[i - 1] < arr[i]:
            if not is_increasing:
                return False
        else:
            if i == 1:
                return False
            if is_increasing:
                is_increasing = False
    if is_increasing:
        return False
    return True
