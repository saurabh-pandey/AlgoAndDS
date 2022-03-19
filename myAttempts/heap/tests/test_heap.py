import pytest

from heap.heap import Heap

class TestMinHeap:
    def test_insert(self):
        h = Heap()
        h.insert(5)
        assert h.top() == 5
        h.insert(3)
        assert h.top() == 3
        h.insert(6)
        assert h.top() == 3
        h.insert(4)
        assert h.top() == 3
    
    def test_pop(self):
        h = Heap()
        h.insert(5)
        h.insert(3)
        h.insert(6)
        h.insert(4)
        assert h.pop() == 3
        assert h.pop() == 4
        assert h.pop() == 5
        h.insert(2)
        h.insert(8)
        assert h.pop() == 2
        assert h.pop() == 6
        assert h.pop() == 8
    
    def test_heapify(self):
        h = Heap()
        h.heapify([5,8,7,2,4,3])
        assert h.top() == 2
        h.insert(1)
        assert h.top() == 1
        assert h.pop() == 1
        assert h.pop() == 2
        h.insert(9)
        assert h.pop() == 3
        h.insert(1)
        assert h.pop() == 1
        assert h.pop() == 4
        assert h.pop() == 5
    
    def test_delete_index(self):
        h = Heap()
        h.insert(5)
        h.insert(3)
        h.insert(7)
        assert h.top() == 3
        assert h.delete_index(0) == 3
        assert h.delete_index(1) == 7
        assert h.delete_index(0) == 5
        h.insert(4)
        assert h.top() == 4
        h.insert(2)
        h.insert(1)
        h.insert(0)
        assert h.delete_index(2) == 2
        assert h.pop() == 0
    
    def test_delete_element(self):
        h = Heap()
        h.heapify([5,8,7,2,4,3])
        assert h.top() == 2
        assert h.delete_element(3) == True
        assert h.delete_element(9) == False
        assert h.delete_element(0) == False
        assert h.delete_element(2) == True
        assert h.top() == 4
        assert h.delete_element(2) == False
        assert h.delete_element(6) == False


class TestMaxHeap:
    def test_insert(self):
        h = Heap(False)
        h.insert(5)
        assert h.top() == 5
        h.insert(3)
        assert h.top() == 5
        h.insert(6)
        assert h.top() == 6
        h.insert(4)
        assert h.top() == 6
    
    def test_pop(self):
        h = Heap(False)
        h.insert(5)
        h.insert(3)
        h.insert(6)
        h.insert(4)
        assert h.pop() == 6
        assert h.pop() == 5
        assert h.pop() == 4
        h.insert(2)
        h.insert(8)
        assert h.pop() == 8
        assert h.pop() == 3
        assert h.pop() == 2
    
    # def test_heapify(self):
    #     h = Heap()
    #     h.heapify([5,8,7,2,4,3])
    #     assert h.top() == 2
    #     h.insert(1)
    #     assert h.top() == 1
    #     assert h.pop() == 1
    #     assert h.pop() == 2
    #     h.insert(9)
    #     assert h.pop() == 3
    #     h.insert(1)
    #     assert h.pop() == 1
    #     assert h.pop() == 4
    #     assert h.pop() == 5
    
    # def test_delete_index(self):
    #     h = Heap()
    #     h.insert(5)
    #     h.insert(3)
    #     h.insert(7)
    #     assert h.top() == 3
    #     assert h.delete_index(0) == 3
    #     assert h.delete_index(1) == 7
    #     assert h.delete_index(0) == 5
    #     h.insert(4)
    #     assert h.top() == 4
    #     h.insert(2)
    #     h.insert(1)
    #     h.insert(0)
    #     assert h.delete_index(2) == 2
    #     assert h.pop() == 0
    
    # def test_delete_element(self):
    #     h = Heap()
    #     h.heapify([5,8,7,2,4,3])
    #     assert h.top() == 2
    #     assert h.delete_element(3) == True
    #     assert h.delete_element(9) == False
    #     assert h.delete_element(0) == False
    #     assert h.delete_element(2) == True
    #     assert h.top() == 4
    #     assert h.delete_element(2) == False
    #     assert h.delete_element(6) == False
