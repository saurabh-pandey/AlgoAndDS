#URL: https://leetcode.com/problems/partition-array-for-maximum-sum/
#Description
"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. 
After partitioning, each subarray has their values changed to become the maximum value of that 
subarray.
Return the largest sum of the given array after partitioning. Test cases are generated so that the a
answer fits in a 32-bit integer.


Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]


Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83


Example 3:

Input: arr = [1], k = 1
Output: 1


Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
"""
def max_sum_partition(arr, k):
    arr_sz = len(arr)
    max_sum = [0 for _ in range(arr_sz + 1)]
    for i in range(1, arr_sz + 1):
        max_subarr_sum = 0
        max_val = 0
        for j in range(1, k + 1):
            if i < j:
                break
            if arr[i - j] > max_val:
                max_val = arr[i - j]
            new_sum = max_sum[i - j] + (j * max_val)
            if new_sum > max_subarr_sum:
                max_subarr_sum = new_sum
        max_sum[i] = max_subarr_sum
    return max_sum[-1]
