from typing import List

def find_N_and_double(nums: List[int]) -> bool:
    for i, n in enumerate(nums):
        for _, m in enumerate(nums[i + 1:]):
            if n == 2 * m:
                return True
            if m == 2 * n:
                return True
    return False
