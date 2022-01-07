#URL: https://leetcode.com/problems/n-th-tribonacci-number/
#Description
"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.


Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4


Example 2:

Input: n = 25
Output: 1389537


Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
def tribonacci(n):
    tribonacci_nums = [-1 for _ in range(n + 1)]
    tribonacci_nums[0] = 0
    if n == 0:
        return 0
    tribonacci_nums[1] = 1
    if n < 3:
        return 1
    tribonacci_nums[2] = 1
    for i in range(3, n + 1):
        tribonacci_nums[i] = (tribonacci_nums[i - 1] +
                              tribonacci_nums[i - 2] +
                              tribonacci_nums[i - 3])
    return tribonacci_nums[n]