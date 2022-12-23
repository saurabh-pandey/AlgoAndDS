import math

from typing import List

def third_max(arr: List[int]) -> int:
    if not arr:
        return None
    
    all_max = []
    for _ in range(3):
        max_val = -math.inf
        for n in arr:
            if all(n < found_max for found_max in all_max):
                if n > max_val:
                    max_val = n
        if not math.isinf(max_val):
            all_max.append(max_val)
    return all_max[2] if len(all_max) == 3 else all_max[0]


