import pytest

import recursion_1.kth_grammer as prob

class TestKthGrammer:
  def test_example1(self):
    n = 1
    k = 1
    res = 0
    assert prob.kthGrammar(n, k) == res
  

  def test_example2(self):
    n = 2
    k = 1
    res = 0
    assert prob.kthGrammar(n, k) == res
  

  def test_example3(self):
    n = 2
    k = 2
    res = 1
    assert prob.kthGrammar(n, k) == res
  

  def test_example4(self):
    n = 3
    k = 1
    res = 0
    assert prob.kthGrammar(n, k) == res
  

  def test_my_example1(self):
    n = 3
    k = 2
    res = 1
    assert prob.kthGrammar(n, k) == res
  

  def test_my_example2(self):
    n = 3
    k = 3
    res = 1
    assert prob.kthGrammar(n, k) == res
  

  def test_my_example3(self):
    n = 3
    k = 4
    res = 0
    assert prob.kthGrammar(n, k) == res