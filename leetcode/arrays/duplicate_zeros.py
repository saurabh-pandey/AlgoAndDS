#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
# Description
"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.
 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]


Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""
def shiftElements(arr, index):
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i-1]

def duplicateZeros(arr):
    i = 0
    while(i < len(arr)):
        if arr[i] == 0:
            shiftElements(arr, i)
            i += 2
        else:
            i += 1
