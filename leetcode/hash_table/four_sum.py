#URL: https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/
#Description
"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of 
tuples (i, j, k, l) such that:
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0


Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0


Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1


Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""
def fillSum(nums1, nums2):
    sz = len(nums1)
    sum12 = {}
    for i in range(sz):
        for j in range(sz):
            sm = nums1[i] + nums2[j]
            if sm in sum12:
                sum12[sm].append((i, j))
            else:
                sum12[sm] = [(i, j)]
    return sum12

def fourSumCount(nums1, nums2, nums3, nums4):
    sum12 = fillSum(nums1, nums2)
    sum34 = fillSum(nums3, nums4)
    count = 0
    for sm in sum12:
        if -sm in sum34:
            count += len(sum12[sm]) * len(sum34[-sm])
    return count