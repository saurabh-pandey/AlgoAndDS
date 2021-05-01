import pytest

import arrays.merge_sorted_array as prob

class TestMergeSortedArray:
  def test_example1(self):
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    prob.merge(nums1, m, nums2, n)
    expected = [1,2,2,3,5,6]
    assert nums1 == expected
  
  def test_example2(self):
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    prob.merge(nums1, m, nums2, n)
    expected = [1]
    assert nums1 == expected
  
  def test_both_empty(self):
    nums1 = []
    m = 0
    nums2 = []
    n = 0
    prob.merge(nums1, m, nums2, n)
    expected = []
    assert nums1 == expected
  
  def test_first_empty(self):
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    prob.merge(nums1, m, nums2, n)
    expected = [1]
    assert nums1 == expected
  
  def test_second_smaller(self):
    nums1 = [7,8,9,0,0,0,0]
    m = 3
    nums2 = [1,2,3,4]
    n = 4
    prob.merge(nums1, m, nums2, n)
    expected = [1,2,3,4,7,8,9]
    assert nums1 == expected
  
  def test_first_smaller(self):
    nums1 = [1,2,4,0,0,0,0]
    m = 3
    nums2 = [6,7,8,9]
    n = 4
    prob.merge(nums1, m, nums2, n)
    expected = [1,2,4,6,7,8,9]
    assert nums1 == expected
  
  def test_alternate(self):
    nums1 = [1,3,5,0,0,0]
    m = 3
    nums2 = [2,4,6]
    n = 3
    prob.merge(nums1, m, nums2, n)
    expected = [1,2,3,4,5,6]
    assert nums1 == expected