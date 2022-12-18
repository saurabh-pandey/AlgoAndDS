from typing import List

def _shift_left(nums: List[int], index: int, shift_by: int) -> None:
    for i in range(index, len(nums) - shift_by):
        nums[i] = nums[i + shift_by]

def remove_elements_1(nums: List[int]) -> int:
    new_len = len(nums)
    end_marker = len(nums)
    dup_count = 0
    i = 1
    while i < end_marker:
        if nums[i - 1] == nums[i]:
            dup_count += 1
            new_len -= 1
        else:
            if dup_count > 0:
                _shift_left(nums, i - dup_count, dup_count)
                end_marker -= dup_count
                i -= dup_count
                dup_count = 0
        i += 1
    return new_len

def remove_elements_2(arr: List[int]) -> int:
    if not arr:
        return 0
    
    write_index = 1
    read_index = 1
    while read_index < len(arr):
        if arr[read_index - 1] != arr[read_index]:
            arr[write_index] = arr[read_index]
            write_index += 1
        read_index += 1
    return write_index
