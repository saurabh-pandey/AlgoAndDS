import pytest
import math

import recursion_1.my_pow as prob

EPSILON = 1.0e-8

class TestMyPow:
  def test_example1(self):
    x = 2.00000
    n = 10
    res = 1024.00000
    assert math.isclose(prob.myPow(x, n), res, rel_tol=EPSILON)
  

  def test_example2(self):
    x = 2.10000
    n = 3
    res = 9.26100
    assert math.isclose(prob.myPow(x, n), res, rel_tol=EPSILON)
  

  def test_example3(self):
    x = 2.00000
    n = -2
    res = 0.25000
    assert math.isclose(prob.myPow(x, n), res, rel_tol=EPSILON)


  def test_my_example1(self):
    x = 2.00000
    n = 8
    res = 256.00000
    assert math.isclose(prob.myPow(x, n), res, rel_tol=EPSILON)
  

  def test_my_example2(self):
    x = 100
    n = 5
    res = 1.00E+10
    assert math.isclose(prob.myPow(x, n), res, rel_tol=EPSILON)

  
  def test_lc_example1(self):
    x = 0.00001
    n = 2147483647
    res = 0.0
    assert math.isclose(prob.myPow(x, n), res, rel_tol=EPSILON)
  

  def test_lc_example2(self):
    x = -1.00000
    n = 2147483647
    res = -1.0
    assert math.isclose(prob.myPow(x, n), res, rel_tol=EPSILON)
  

  