#URL: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
# Description
"""
Given a binary array, find the maximum number of consecutive 1s in this array.


Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.


Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
def findMaxConsecutiveOnes(nums):
    maxCount = 0
    count = 0
    for n in nums:
        if n != 1:
            count = 0
        else:
            count += 1
            if (count > maxCount):
                maxCount = count
    return maxCount

def test1():
    nums =  [1,1,0,1,1,1]
    maxOnes = findMaxConsecutiveOnes(nums)
    if maxOnes == 3:
        print(f'SUCCESS: max consecutive ones for array {nums} equals {maxOnes}')
    else:
        print(f'FAILURE: max consecutive ones for array {nums} equals {maxOnes}, but expected 3')

def test2():
    nums =  [0, 0, 0]
    maxOnes = findMaxConsecutiveOnes(nums)
    if maxOnes == 0:
        print(f'SUCCESS: max consecutive ones for array {nums} equals {maxOnes}')
    else:
        print(f'FAILURE: max consecutive ones for array {nums} equals {maxOnes}, but expected 3')

def test3():
    nums =  [1,1,1,1]
    maxOnes = findMaxConsecutiveOnes(nums)
    if maxOnes == 4:
        print(f'SUCCESS: max consecutive ones for array {nums} equals {maxOnes}')
    else:
        print(f'FAILURE: max consecutive ones for array {nums} equals {maxOnes}, but expected 3')

def test4():
    nums =  []
    maxOnes = findMaxConsecutiveOnes(nums)
    if maxOnes == 0:
        print(f'SUCCESS: max consecutive ones for array {nums} equals {maxOnes}')
    else:
        print(f'FAILURE: max consecutive ones for array {nums} equals {maxOnes}, but expected 3')

def test5():
    nums =  [1]
    maxOnes = findMaxConsecutiveOnes(nums)
    if maxOnes == 1:
        print(f'SUCCESS: max consecutive ones for array {nums} equals {maxOnes}')
    else:
        print(f'FAILURE: max consecutive ones for array {nums} equals {maxOnes}, but expected 3')

def test6():
    nums =  [0,1]
    maxOnes = findMaxConsecutiveOnes(nums)
    if maxOnes == 1:
        print(f'SUCCESS: max consecutive ones for array {nums} equals {maxOnes}')
    else:
        print(f'FAILURE: max consecutive ones for array {nums} equals {maxOnes}, but expected 3')

def run():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

run()
