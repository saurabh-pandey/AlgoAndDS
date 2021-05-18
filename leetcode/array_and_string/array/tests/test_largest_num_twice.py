import pytest

import array_and_string.array.largest_num_twice as prob

class TestLargestNumTwice:
  def test_example1(self):
    nums = [3,6,1,0]
    assert prob.dominantIndex(nums) == 1
  

  def test_example2(self):
    nums = [1,2,3,4]
    assert prob.dominantIndex(nums) == -1
  

  def test_example3(self):
    nums = [1]
    assert prob.dominantIndex(nums) == 0
  

  def test_empty(self):
    nums = []
    assert prob.dominantIndex(nums) == -1