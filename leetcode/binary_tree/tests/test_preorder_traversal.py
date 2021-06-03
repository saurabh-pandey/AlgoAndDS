import pytest

import binary_tree.preorder_traversal as prob

class TestPreorderTraversal:
  def test_example1(self):
    root = [1,None,2,3]
    Output: [1,2,3]