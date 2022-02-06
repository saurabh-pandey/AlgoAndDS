#Description
"""
While solving a leetcode problem (https://leetcode.com/problems/partition-array-for-maximum-sum/) I 
accidently solved a slightly different problem. The problem that I actually solved is described 
aabelow:
Given an integer array arr, partition the array into (contiguous) k subarrays. After partitioning, 
each subarray has their values changed to become the maximum value of that subarray. Return the 
largest sum of the given array after partitioning. Test cases are generated so that the a answer 
fits in a 32-bit integer.


Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 86
Explanation: arr becomes [1,15,15,15,15,15,10]


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
def done_partitioning(partitions, count, sz):
    if not partitions:
        return count > 0
    if partitions[-1] < sz - 1:
        return False
    for i in range(len(partitions) - 1, 0, -1):
        if partitions[i - 1] < partitions[i] - 1:
            return False
    return True

def increment_partition(partitions, sz):
    if not partitions:
        return
    if partitions[-1] < sz - 1:
        partitions[-1] += 1
        return
    else:
        for i in range(len(partitions) - 1, 0, -1):
            if partitions[i - 1] < partitions[i] - 1:
                partitions[i - 1] += 1
                partitions[i] = partitions[i - 1] + 1
                return

def max_partition(arr, k):
    arr_sz = len(arr)
    partitions = [i for i in range(1, k)]
    max_sum = 0
    count = 0
    while(not done_partitioning(partitions, count, arr_sz)):
        start = 0
        arr_sum = 0
        for p in partitions:
            max_subarray_val = max(arr[start : p])
            arr_sum += max_subarray_val * (p - start)
            start = p
        if start < arr_sz:
            max_subarray_val = max(arr[start:])
            arr_sum += max_subarray_val * (arr_sz - start)
        if arr_sum > max_sum:
            max_sum = arr_sum
        increment_partition(partitions, arr_sz)
        count += 1
    return max_sum
        