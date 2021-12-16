#URL: https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
#Description
"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""
import math

def isHappy(n) -> bool:
    unq_nums = set()
    new_num = n
    while new_num != 1:
        if new_num in unq_nums:
            return False
        unq_nums.add(new_num)
        num_digits = int(math.log10(new_num)) + 1
        n = new_num
        new_num = 0
        for i in range(num_digits, 0, -1):
            place_val = 10**(i - 1)
            d = int(n/place_val)
            new_num += d*d
            n -= d * place_val
    return True
