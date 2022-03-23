#Description
"""
Given a stream of numbers compute the running median.

NOTE: This problem was discussed in Tim's algo-1 course as an application of heap.
"""
from heap.heap import Heap


class MedianCalculator:
    def __init__(self) -> None:
        self.max_heap = Heap(False)
        self.min_heap = Heap()

    def add(self, num):
        # print("\nAdding ", num)
        # print("Max Heap = ", self.max_heap.vals)
        # print("Min Heap = ", self.min_heap.vals)
        max_heap_sz = self.max_heap.size()
        min_heap_sz = self.min_heap.size()
        total_sz = max_heap_sz + min_heap_sz
        if total_sz == 0:
            self.max_heap.insert(num)
        else:
            max_val = self.max_heap.top()
            if min_heap_sz == 0:
                if num < max_val:
                    old_max_val = self.max_heap.pop()
                    self.max_heap.insert(num)
                    self.min_heap.insert(old_max_val)
                else:
                    self.min_heap.insert(num)
            else:
                min_val = self.min_heap.top()
                if num < max_val:
                    if max_heap_sz == min_heap_sz:
                        self.max_heap.insert(num)
                    else:
                        old_max_val = self.max_heap.pop()
                        # print("  Popped Max Heap = ", self.max_heap.vals)
                        self.max_heap.insert(num)
                        self.min_heap.insert(old_max_val)
                elif num > min_val:
                    if max_heap_sz == min_heap_sz:
                        old_min_val = self.min_heap.pop()
                        self.min_heap.insert(num)
                        self.max_heap.insert(old_min_val)
                    else:
                        self.min_heap.insert(num)
                else:
                    if max_heap_sz == min_heap_sz:
                        self.max_heap.insert(num)
                    else:
                        self.min_heap.insert(num)
        # print("After add")
        # print("Max Heap = ", self.max_heap.vals)
        # print("Min Heap = ", self.min_heap.vals)


    def median(self):
        max_heap_sz = self.max_heap.size()
        min_heap_sz = self.min_heap.size()
        total_sz = max_heap_sz + min_heap_sz
        max_val = self.max_heap.top()
        min_val = self.min_heap.top()
        if total_sz == 0:
            return None
        else:
            assert self.check_invariant(), "Invariants not satisfied"
            if total_sz % 2 == 0:
                return (min_val + max_val)/2
            else:
                return max_val
    
    def check_invariant(self):
        max_heap_sz = self.max_heap.size()
        min_heap_sz = self.min_heap.size()
        if max_heap_sz == min_heap_sz:
            return True
        elif max_heap_sz == (min_heap_sz + 1):
            return True
        return False