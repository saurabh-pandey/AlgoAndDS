from typing import List

def _shift_left(nums: List[int], index: int, shift_by: int) -> None:
    for i in range(index, len(nums) - shift_by):
        nums[index] = nums[index + shift_by]

def remove_elements(nums: List[int], val: int) -> int:
    for i in range(len(nums)):
        pass
