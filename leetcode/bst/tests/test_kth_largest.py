import pytest

from bst.kth_largest import KthLargest

class TestKthLargest:
    def test_example1(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        kthLargest.new_add(3)
        assert kthLargest.add(3) == 4
        kthLargest.new_add(5)
        assert kthLargest.add(5) == 5
        assert kthLargest.add(10) == 5
        assert kthLargest.add(9) == 8
        assert kthLargest.add(4) == 8