import pytest

import recursion_1.fibonacci_numbers as prob

class TestFibonacciNumbers:
  def test_example1(self):
    n = 2
    res = 1
    assert prob.fib(n) == res
  

  def test_example2(self):
    n = 3
    res = 2
    assert prob.fib(n) == res
  

  def test_example3(self):
    n = 4
    res = 3
    assert prob.fib(n) == res
  

  def test_my_example1(self):
    n = 0
    res = 0
    assert prob.fib(n) == res
  

  def test_my_example2(self):
    n = 1
    res = 1
    assert prob.fib(n) == res