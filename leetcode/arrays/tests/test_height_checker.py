import pytest

import arrays.height_checker as prob

class TestHeightChecker:
  def test_example1(self):
    heights = [1,1,4,2,1,3]
    numSelected = prob.heightChecker(heights)
    assert numSelected == 3
  
  def test_example2(self):
    heights = [5,1,2,3,4]
    numSelected = prob.heightChecker(heights)
    assert numSelected == 5
  
  def test_example3(self):
    heights = [1,2,3,4,5]
    numSelected = prob.heightChecker(heights)
    assert numSelected == 0
  
  def test_empty(self):
    heights = []
    numSelected = prob.heightChecker(heights)
    assert numSelected == 0
  
  def test_reverse(self):
    heights = [5,4,3,2,1]
    numSelected = prob.heightChecker(heights)
    assert numSelected == 4