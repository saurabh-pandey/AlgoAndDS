#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

def shiftByOne(arr, start, end):
    for i in range(end, start, -1):
        arr[i] = arr[i - 1]

def merge(nums1, m, nums2, n) -> None:
    if n == 0:
        return
    
    i = 0
    j = 0
    totalSz = m + n
    while i < totalSz:
        if j < n and nums2[j] < nums1[i]:
            shiftByOne(nums1, i, totalSz-1)
            nums1[i] = nums2[j]
            j += 1
        if j < n and i - j >= m:
            nums1[i] = nums2[j]
            j += 1
        i += 1


def test1():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    result = [1,2,2,3,5,6]
    if result == nums1:
        print("Success in test1")
    else:
        print(f'Failure in test1 nums1 = {nums1}, result = {result}')

def test2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    result = [1]
    if result == nums1:
        print("Success in test2")
    else:
        print(f'Failure in test2 nums1 = {nums1}, result = {result}')

def test3():
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    merge(nums1, m, nums2, n)
    result = [1,2,3,4,5,6]
    if result == nums1:
        print("Success in test3")
    else:
        print(f'Failure in test3 nums1 = {nums1}, result = {result}')

def run():
    test1()
    test2()
    test3()

run()