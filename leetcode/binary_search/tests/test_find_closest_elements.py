import pytest

import binary_search.find_closest_elements as prob

class TestFindClosestElements:
  def test_example1(self):
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    res = [1,2,3,4]
    assert prob.findClosestElements(arr, k, x) == res
  
  def test_example2(self):
    arr = [1,2,3,4,5]
    k = 4
    x = -1
    res = [1,2,3,4]
    assert prob.findClosestElements(arr, k, x) == res
  
  def test_all_elem(self):
    arr = [1,2,3,4]
    k = 4
    x = 2
    res = [1,2,3,4]
    assert prob.findClosestElements(arr, k, x) == res
  
  def test_beyond_max(self):
    arr = [1,2,3,4,5,6]
    k = 5
    x = 9
    res = [2,3,4,5,6]
    assert prob.findClosestElements(arr, k, x) == res
  
  def test_lc1(self):
    arr = [0,0,1,2,3,3,4,7,7,8]
    k = 3
    x = 5
    res = [3,3,4]
    assert prob.findClosestElements(arr, k, x) == res
  
  def test_lc2(self):
    arr = [0,0,0,1,3,5,6,7,8,8]
    k = 2
    x = 2
    res = [1, 3]
    assert prob.findClosestElements(arr, k, x) == res
  
  def test_lc3(self):
    arr = [1,3]
    k = 1
    x = 2
    res = [1]
    assert prob.findClosestElements(arr, k, x) == res