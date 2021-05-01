import pytest

import arrays.find_N_and_double as prob

class TestFindNumAndDoble:
  def test_example1(self):
    assert prob.find_N_and_double([10,2,5,3]) == True
  
  def test_example2(self):
    assert prob.find_N_and_double([7,1,14,11]) == True
  
  def test_example3(self):
    assert prob.find_N_and_double([3,1,7,11]) == False
  
  def test_empty(self):
    assert prob.find_N_and_double([]) == False
  
  def test_size_1(self):
    assert prob.find_N_and_double([1]) == False
  
  def test_repetition(self):
    assert prob.find_N_and_double([1,1]) == False