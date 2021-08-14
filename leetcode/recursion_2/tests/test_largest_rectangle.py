import pytest

import recursion_2.largest_rectangle as prob

class TestLargestRectangle:
  def test_example1(self):
    heights = [2,1,5,6,2,3]
    res = 10
    assert prob.largestRectangleArea(heights) == res
  
  
  def test_example2(self):
    heights = [2,4]
    res = 4
    assert prob.largestRectangleArea(heights) == res
  

  def test_my_example1(self):
    heights = [1,2,3,4,5,6]
    res = 12
    assert prob.largestRectangleArea(heights) == res
  

  def test_my_example2(self):
    heights = [6,5,4,3,2,1]
    res = 12
    assert prob.largestRectangleArea(heights) == res
  

  def test_lc_example1(self):
    heights = [1,1]
    res = 2
    assert prob.largestRectangleArea(heights) == res
  

  def test_my_example3(self):
    heights = [1,1,1,1,1,1,1,1]
    res = 8
    assert prob.largestRectangleArea(heights) == res