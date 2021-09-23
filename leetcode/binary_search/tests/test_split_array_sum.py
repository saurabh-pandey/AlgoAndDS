import pytest

import binary_search.split_array_sum as prob

class TestSplitArraySum:
  def test_example1(self):
    nums = [7,2,5,10,8]
    m = 2
    res = 18
    assert prob.splitArray(nums, m) == res