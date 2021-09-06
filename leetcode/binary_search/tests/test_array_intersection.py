import pytest

import binary_search.array_intersection as prob

class TestArrayIntersection:
  def test_example1(self):
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = [2]
    assert prob.intersection(nums1, nums2) == set(res)
  
  def test_example2(self):
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res = [9,4]
    assert prob.intersection(nums1, nums2) == set(res)
  
  def test_empty_1(self):
    nums1 = []
    nums2 = [9,4,9,8,4]
    res = []
    assert prob.intersection(nums1, nums2) == set(res)
  
  def test_empty_2(self):
    nums1 = [4,9,5]
    nums2 = []
    res = []
    assert prob.intersection(nums1, nums2) == set(res)