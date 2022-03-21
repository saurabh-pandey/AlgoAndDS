#Description
"""
Given a stream of numbers compute the running median.

NOTE: This problem was discussed in Tim's algo-1 course as an application of heap.
"""
from heap import Heap


class MedianCalculator:
    def __init__(self) -> None:
        self.max_heap = Heap(False)
        self.min_heap = Heap()

    def add(self, num):
        # Assuming that max_heap is always the bigger one
        # If max_heap is same as min_heap after insert max_heap will be bigger
        # If max_heap is bigger then they have two option:
        #   1. Either max_heap stays biggger
        #   2. Or they become equal
        # max_heap being smaller will be breaking the invariant
        max_heap_sz = self.max_heap.size()
        min_heap_sz = self.min_heap.size()
        # Invariant
        # min_heap_sz == max_heap_sz or (min_heap_sz - max_heap_sz) == 1
        if max_heap_sz == 0:
            self.max_heap.insert(num)
        max_val = self.max_heap.top()
        min_val = self.min_heap.top()
        if num <= max_val:
            # Add to max_heap

            pass
        elif num >= min_val:
            # Add to min_heap
            pass
        else:
            # Add to either but maintaining the invariant
            pass


    def median(self):
        max_heap_sz = self.max_heap.size()
        min_heap_sz = self.min_heap.size()
        total_sz = max_heap_sz + min_heap_sz
        max_val = self.max_heap.top()
        min_val = self.min_heap.top()
        if total_sz % 2 == 0:
            return (min_val + max_val)/2
        else:
            # return min or max val depending on which is bigger
            pass