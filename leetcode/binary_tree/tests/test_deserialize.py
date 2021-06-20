import pytest

from binary_tree.deserialize import deserialize
from binary_tree.serialize import serialize
import binary_tree.operations as bTree

class TestSerialize:
  def test_example1(self):
    root = [1,2,3,None,None,4,5]
    treeStr = ",".join(map(str, root))
    rootNode = deserialize(treeStr)
    assert serialize(rootNode) == treeStr
  

  def test_example2(self):
    root = []
    treeStr = ",".join(map(str, root))
    rootNode = deserialize(treeStr)
    assert serialize(rootNode) == treeStr
  

  # def test_example2(self):
  #   root = []
  #   res = ",".join(map(str, root))
  #   rootNode = bTree.create(root)
  #   assert prob.serialize(rootNode) == res
  

  # def test_example3(self):
  #   root = [1]
  #   res = ",".join(map(str, root))
  #   rootNode = bTree.create(root)
  #   assert prob.serialize(rootNode) == res
  

  # def test_example4(self):
  #   root = [1,2]
  #   res = ",".join(map(str, root))
  #   rootNode = bTree.create(root)
  #   assert prob.serialize(rootNode) == res