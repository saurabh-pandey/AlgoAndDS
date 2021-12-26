#URL: https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
#Description
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return 
the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's 
size.
"""
def topKFrequent(nums, k):
    nums_freq = {}
    for n in nums:
        if n in nums_freq:
            nums_freq[n] += 1
        else:
            nums_freq[n] = 1

    top_k = [0 for _ in range(k)]
    count = 0 
    for n, _ in sorted(nums_freq.items(), key=lambda item: item[1], reverse=True):
        if count == k:
            break
        top_k[count] = n
        count += 1
    return top_k