from typing import List

def height_checker(arr: List[int]) -> None:
    expected = sorted(arr)
    num_mismatch = 0
    for n, m in zip(arr, expected):
        if n != m:
            num_mismatch += 1
    return num_mismatch
