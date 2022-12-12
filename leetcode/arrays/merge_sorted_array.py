#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
# Description
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]


Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
"""

def shift_by_one(arr, start, end):
    for i in range(end, start, -1):
        arr[i] = arr[i - 1]

def merge(nums1, m, nums2, n) -> None:
    if n == 0:
        return
    
    i = 0
    j = 0
    total_sz = m + n
    while i < total_sz:
        if j < n and nums2[j] < nums1[i]:
            shift_by_one(nums1, i, total_sz - 1)
            nums1[i] = nums2[j]
            j += 1
        if (j < n) and (i - j >= m):
            nums1[i] = nums2[j]
            j += 1
        i += 1
