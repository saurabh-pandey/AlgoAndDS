import pytest

import binary_tree.serialize as prob
import binary_tree.operations as bTree

class TestSerialize:
  def test_example1(self):
    root = [1,2,3,None,None,4,5]
    res = ",".join(map(str, root))
    rootNode = bTree.create(root)
    assert prob.serialize(rootNode) == res
  

  def test_example2(self):
    root = []
    res = ",".join(map(str, root))
    rootNode = bTree.create(root)
    assert prob.serialize(rootNode) == res
  

  def test_example3(self):
    root = [1]
    res = ",".join(map(str, root))
    rootNode = bTree.create(root)
    assert prob.serialize(rootNode) == res
  

  def test_example4(self):
    root = [1,2]
    res = ",".join(map(str, root))
    rootNode = bTree.create(root)
    assert prob.serialize(rootNode) == res