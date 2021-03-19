# URL: https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
# Description
"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.


Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.


Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
 

Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""

def find_N_and_double(arr):
    length = len(arr)
    if length < 2:
        return False
    
    for i in range(length):
        for j in range(i + 1, length):
            if (arr[i] == (2 * arr[j])):
                return True
            elif (arr[j] == (2 * arr[i])):
                return True

    return False

def test1():
    arr = [10,2,5,3]
    found = find_N_and_double(arr)
    if found:
        print(f'SUCCESS: for array {arr}')
    else:
        print(f'FAILURE: for array {arr}')

def test2():
    arr = [7,1,14,11]
    found = find_N_and_double(arr)
    if found:
        print(f'SUCCESS: for array {arr}')
    else:
        print(f'FAILURE: for array {arr}')

def test3():
    arr = [3,1,7,11]
    found = find_N_and_double(arr)
    if not found:
        print(f'SUCCESS: for array {arr}')
    else:
        print(f'FAILURE: for array {arr}')

def test4():
    arr = []
    found = find_N_and_double(arr)
    if not found:
        print(f'SUCCESS: for array {arr}')
    else:
        print(f'FAILURE: for array {arr}')

def test5():
    arr = [1]
    found = find_N_and_double(arr)
    if not found:
        print(f'SUCCESS: for array {arr}')
    else:
        print(f'FAILURE: for array {arr}')

def test6():
    arr = [2,2]
    found = find_N_and_double(arr)
    if not found:
        print(f'SUCCESS: for array {arr}')
    else:
        print(f'FAILURE: for array {arr}')

def run():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

run()