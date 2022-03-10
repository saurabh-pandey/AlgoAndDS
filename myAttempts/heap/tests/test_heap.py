import imp
import pytest

from heap.heap import Heap

class TestHeap:
    def test_example1(self):
        h = Heap()
        h.insert(5)
        assert h.extract_min() == 5
        h.insert(3)
        assert h.extract_min() == 3
        h.insert(6)
        assert h.extract_min() == 3
        h.insert(4)
        assert h.extract_min() == 3
