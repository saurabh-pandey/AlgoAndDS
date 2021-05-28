import pytest

import array_and_string.array.two_num_sum as prob

class TestTwoNumSum:
  def test_example1(self):
    numbers = [2,7,11,15]
    target = 9
    result = [1,2]
    print(f'TwoSum = {prob.twoSum(numbers, target)}')
    assert prob.twoSum(numbers, target) == result
  
  
  def test_example2(self):
    numbers = [2,3,4]
    target = 6
    result = [1,3]
    print(f'TwoSum = {prob.twoSum(numbers, target)}')
    assert prob.twoSum(numbers, target) == result
  

  def test_example3(self):
    numbers = [-1,0]
    target = -1
    result = [1,2]
    print(f'TwoSum = {prob.twoSum(numbers, target)}')
    assert prob.twoSum(numbers, target) == result
  

  def test_empty(self):
    numbers = []
    target = 0
    result = -1
    print(f'TwoSum = {prob.twoSum(numbers, target)}')
    assert prob.twoSum(numbers, target) == result
  

  def test_single(self):
    numbers = [1]
    target = 1
    result = -1
    print(f'TwoSum = {prob.twoSum(numbers, target)}')
    assert prob.twoSum(numbers, target) == result
  

  def test_not_found(self):
    numbers = [1,2]
    target = 5
    result = -1
    print(f'TwoSum = {prob.twoSum(numbers, target)}')
    assert prob.twoSum(numbers, target) == result