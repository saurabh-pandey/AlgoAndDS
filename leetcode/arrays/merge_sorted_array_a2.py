from typing import List

def shift_right(nums: List[int], index: int) -> None:
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = 1
    j = 0
    while i < m + n:
        if i - j == m and j < n:
            nums1[i] = nums2[j]
            j += 1
        elif j < n and nums1[i] > nums2[j]:
            shift_right(nums1, i)
            nums1[i] = nums2[j]
            j += 1
        i += 1
