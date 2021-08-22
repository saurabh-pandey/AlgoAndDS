import pytest

import recursion_2.skyline as prob

class TestSkyline:
  # def test_example1(self):
  #   buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
  #   res = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
  #   assert prob.getSkyline(buildings) == res

  def test_single(self):
    buildings = [[1,3,4]]
    res = [[1,3,4]]
    assert prob.getSkyline(buildings) == res

  def test_two_spaced(self):
    buildings = [[1,3,4], [4,6,5]]
    res = [[1,3,4],[3,4,0],[4,6,5]]
    assert prob.getSkyline(buildings) == res
  
  def test_two_intersect(self):
    buildings = [[1,3,4], [2,6,1]]
    res = [[1,3,4],[3,6,1]]
    assert prob.getSkyline(buildings) == res
  
  def test_two_intersect_1(self):
    buildings = [[1,3,4], [2,6,5]]
    res = [[1,2,4],[2,6,5]]
    assert prob.getSkyline(buildings) == res
  
  def test_two_adjoint_merge(self):
    buildings = [[1,3,4], [3,6,4]]
    res = [[1,6,4]]
    assert prob.getSkyline(buildings) == res
  
  def test_two_intersect_merge(self):
    buildings = [[1,3,4], [2,6,4]]
    res = [[1,6,4]]
    assert prob.getSkyline(buildings) == res
  
  def test_two_same_merge(self):
    buildings = [[1,3,4], [1,3,4]]
    res = [[1,3,4]]
    assert prob.getSkyline(buildings) == res
  
  def test_one_inside_merge(self):
    buildings = [[1,6,4], [2,3,4]]
    res = [[1,6,4]]
    assert prob.getSkyline(buildings) == res
  
  def test_one_small_inside_merge(self):
    buildings = [[1,6,4], [2,3,2]]
    res = [[1,6,4]]
    assert prob.getSkyline(buildings) == res