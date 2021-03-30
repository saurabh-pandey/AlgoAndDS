import pytest

import find_disappeared_nums as prob

class TestFindDisappearedNumbers:
  def test_example1(self):
    nums = [4,3,2,7,8,2,3,1]
    disapperedNums = prob.findDisappearedNumbers(nums)
    expected = [5,6]
    assert disapperedNums == expected
  
  def test_example2(self):
    nums = [1,1]
    disapperedNums = prob.findDisappearedNumbers(nums)
    expected = [2]
    assert disapperedNums == expected
  
  def test_empty(self):
    nums = []
    disapperedNums = prob.findDisappearedNumbers(nums)
    expected = []
    assert disapperedNums == expected
  
  def test_single(self):
    nums = [1]
    disapperedNums = prob.findDisappearedNumbers(nums)
    expected = [1]
    assert disapperedNums == expected