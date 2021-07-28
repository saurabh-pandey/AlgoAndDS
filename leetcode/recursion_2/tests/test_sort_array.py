import pytest

import recursion_2.sort_array as prob

class TestSortArray:
  def test_example1(self):
    nums = [5,2,3,1]
    res = [1,2,3,5]
    assert prob.sortArray(nums) == res
    # assert prob.sortArray(nums, True) == res