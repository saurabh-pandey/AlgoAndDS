import pytest

import binary_search.array_intersection_2 as prob

class TestArrayIntersection2:
  def test_example1(self):
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = [2,2]
    assert prob.intersect(nums1, nums2) == res
  
  def test_example2(self):
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res = [4,9]
    assert prob.intersect(nums1, nums2) == res
  
  def test_empty_1(self):
    nums1 = []
    nums2 = [9,4,9,8,4]
    res = []
    assert prob.intersect(nums1, nums2) == res
  
  def test_empty_2(self):
    nums1 = [4,9,5]
    nums2 = []
    res = []
    assert prob.intersect(nums1, nums2) == res