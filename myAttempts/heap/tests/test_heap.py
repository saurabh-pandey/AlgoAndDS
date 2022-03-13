import pytest

from heap.heap import Heap

class TestHeap:
    def test_insert(self):
        h = Heap()
        h.insert(5)
        assert h.get_min() == 5
        h.insert(3)
        assert h.get_min() == 3
        h.insert(6)
        assert h.get_min() == 3
        h.insert(4)
        assert h.get_min() == 3
    
    def test_extract_min(self):
        h = Heap()
        h.insert(5)
        h.insert(3)
        h.insert(6)
        h.insert(4)
        assert h.extract_min() == 3
        assert h.extract_min() == 4
        assert h.extract_min() == 5
        h.insert(2)
        h.insert(8)
        assert h.extract_min() == 2
        assert h.extract_min() == 6
        assert h.extract_min() == 8
    
    def test_heapify(self):
        h = Heap()
        h.heapify([5,8,7,2,4,3])
        assert h.get_min() == 2
        h.insert(1)
        assert h.get_min() == 1
        assert h.extract_min() == 1
        assert h.extract_min() == 2
        h.insert(9)
        assert h.extract_min() == 3
        h.insert(1)
        assert h.extract_min() == 1
        assert h.extract_min() == 4
        assert h.extract_min() == 5
    
    # def test_delete(self):
    #     h = Heap()
    #     h.insert(5)
    #     assert h.extract_min() == 5
    #     h.insert(3)
    #     assert h.extract_min() == 3
    #     h.delete(3)
    #     assert h.extract_min() == 5
    #     h.insert(4)
    #     assert h.extract_min() == 3
    #     h.insert(2)
    #     assert h.extract_min() == 2
    #     h.delete(2)
    #     assert h.extract_min() == 3
