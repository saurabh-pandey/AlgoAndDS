import pytest
import math

import binary_search.median_sorted_arrays as prob

class TestMedianSortedArrays:
  def test_example1(self):
    nums1 = [1,3]
    nums2 = [2]
    res = 2.00000
    assert math.isclose(prob.findMedianSortedArrays(nums1, nums2), res)
  
  def test_example2(self):
    nums1 = [1,2]
    nums2 = [3,4]
    res = 2.5
    assert math.isclose(prob.findMedianSortedArrays(nums1, nums2), res)
  
  def test_example3(self):
    nums1 = [0,0]
    nums2 = [0,0]
    res = 0.0
    assert math.isclose(prob.findMedianSortedArrays(nums1, nums2), res)
  
  def test_example4(self):
    nums1 = []
    nums2 = [1]
    res = 1.0
    assert math.isclose(prob.findMedianSortedArrays(nums1, nums2), res)
  
  def test_example5(self):
    nums1 = [2]
    nums2 = []
    res = 2.0
    assert math.isclose(prob.findMedianSortedArrays(nums1, nums2), res)