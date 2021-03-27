import pytest

import remove_element as prob

class TestRemoveElement:
  def test_example1(self):
    nums = [3,2,2,3]
    val = 3
    newLen = prob.removeElement(nums, val)
    assert newLen == 2
    expected = [2,2]
    assert expected == nums[:newLen]
  
  def test_example2(self):
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    newLen = prob.removeElement(nums, val)
    assert newLen == 5
    expected = [0,1,4,0,3]
    assert expected == nums[:newLen]
  
  def test_empty(self):
    nums = []
    val = 2
    newLen = prob.removeElement(nums, val)
    assert newLen == 0
    expected = []
    assert expected == nums
  
  def test_remove_all(self):
    nums = [1,1,1]
    val = 1
    newLen = prob.removeElement(nums, val)
    assert newLen == 0
    expected = []
    assert expected == nums[:newLen]
  
  def test_remove_none(self):
    nums = [2,2,2]
    val = 1
    newLen = prob.removeElement(nums, val)
    assert newLen == 3
    expected = [2,2,2]
    assert expected == nums[:newLen]
  
  def test_another_example(self):
    nums = [0,4,4,0,4,4,4,0,2]
    val = 4
    newLen = prob.removeElement(nums, val)
    assert newLen == 4
    expected = [0,2,0,0]
    assert expected == nums[:newLen]
  