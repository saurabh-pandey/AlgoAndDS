from typing import List

def _shift_left(arr: List[int], index: int) -> None:
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

def move_zeros_v1(arr: List[int]) -> None:
    curr_index = 0
    zero_index = len(arr) - 1
    while curr_index < zero_index:
        if arr[curr_index] == 0:
            _shift_left(arr, curr_index)
            arr[zero_index] = 0
            zero_index -= 1
        else:
            curr_index += 1
    
def move_zeros_v2(arr: List[int]) -> None:
    write_index = 0
    read_index = 0
    while write_index < len(arr):
        if read_index == len(arr):
            arr[write_index] = 0
            write_index += 1
        else:
            if arr[read_index] != 0:
                arr[write_index] = arr[read_index]
                write_index += 1
            read_index += 1
