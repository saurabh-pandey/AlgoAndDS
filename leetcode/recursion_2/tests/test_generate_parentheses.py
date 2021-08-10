import pytest

import recursion_2.generate_parentheses as prob


class TestGenerateParentheses:
  def test_example1(self):
    n = 3
    res = ["((()))","(()())","(())()","()(())","()()()"]
    print(prob.generateParenthesis(n))