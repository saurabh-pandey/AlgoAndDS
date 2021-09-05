import pytest

import binary_search.next_greater_letter as prob

class TestNextGreatestLetter:
  def test_example1(self):
    letters = ["c","f","j"]
    target = "a"
    res = "c"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_example2(self):
    letters = ["c","f","j"]
    target = "c"
    res = "f"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_example3(self):
    letters = ["c","f","j"]
    target = "d"
    res = "f"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_example4(self):
    letters = ["c","f","j"]
    target = "g"
    res = "j"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_example5(self):
    letters = ["c","f","j"]
    target = "j"
    res = "c"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_double_1(self):
    letters = ["c", "f"]
    target = "a"
    res = "c"
    assert prob.nextGreatestLetter(letters, target) == res

  def test_double_2(self):
    letters = ["c", "f"]
    target = "c"
    res = "f"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_double_3(self):
    letters = ["c", "f"]
    target = "e"
    res = "f"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_double_4(self):
    letters = ["c", "f"]
    target = "f"
    res = "c"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_double_5(self):
    letters = ["c", "f"]
    target = "h"
    res = "c"
    assert prob.nextGreatestLetter(letters, target) == res
  
  def test_duplicates(self):
    letters = ["c", "c", "f", "f"]
    target = "c"
    res = "f"
    assert prob.nextGreatestLetter(letters, target) == res