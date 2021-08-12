import pytest

import recursion_2.generate_parentheses as prob


class TestGenerateParentheses:
  def test_example1(self):
    n = 3
    res = {"((()))","(()())","(())()","()(())","()()()"}
    out = prob.generateParenthesis(n)
    assert res == set(out)
  

  def test_example2(self):
    n = 1
    res = {"()"}
    out = prob.generateParenthesis(n)
    assert res == set(out)
  

  def test_my_example1(self):
    n = 2
    res = {"(())", "()()"}
    out = prob.generateParenthesis(n)
    assert res == set(out)