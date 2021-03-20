import pytest

import valid_mountain_array as prob

class TestValidMountainArray:
  def test_example1(self):
    assert prob.validMountainArray([2,1]) == False
  
  def test_example2(self):
    assert prob.validMountainArray([3,5,5]) == False
  
  def test_example3(self):
    assert prob.validMountainArray([0,3,2,1]) == True
  
  def test_empty(self):
    assert prob.validMountainArray([]) == False
  
  def test_len_1(self):
    assert prob.validMountainArray([2]) == False
  
  def test_all_equal(self):
    assert prob.validMountainArray([1,1,1,1]) == False
  
  def test_some_equal(self):
    assert prob.validMountainArray([0,1,2,2]) == False
  
  def test_oscillation(self):
    assert prob.validMountainArray([1,4,2,7,3]) == False
  
  def test_ascending_only(self):
    assert prob.validMountainArray([1,2,3,4,5]) == False
  
  def test_descending_only(self):
    assert prob.validMountainArray([5,4,3,2,1,0]) == False

  def test_another_valid(self):
    assert prob.validMountainArray([0,1,2,3,4,5,4,3,2,1,0]) == True