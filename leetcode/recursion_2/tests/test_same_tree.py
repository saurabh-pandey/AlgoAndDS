import pytest

import binary_tree.operations as bTree
import recursion_2.same_tree as prob


class TestSameTree:
  def test_example1(self):
    p = [1,2,3]
    q = [1,2,3]
    res = True
    pRoot = bTree.create(p)
    qRoot = bTree.create(q)
    assert prob.isSameTree(pRoot, qRoot) == res
    assert prob.isSameTree(pRoot, qRoot, False) == res
  

  def test_example2(self):
    p = [1,2]
    q = [1,None,2]
    res = False
    pRoot = bTree.create(p)
    qRoot = bTree.create(q)
    assert prob.isSameTree(pRoot, qRoot) == res
    assert prob.isSameTree(pRoot, qRoot, False) == res
  

  def test_example3(self):
    p = [1,2,1]
    q = [1,1,2]
    res = False
    pRoot = bTree.create(p)
    qRoot = bTree.create(q)
    assert prob.isSameTree(pRoot, qRoot) == res
    assert prob.isSameTree(pRoot, qRoot, False) == res