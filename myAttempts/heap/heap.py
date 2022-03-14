#Description
"""
A heap data structure. It supports the follwoing operations:
insert(elem) => O(log N)
extract_min() => O(log N)
delete(N) => O(log N)
heapify(arr) => O(N)

NOTE: This is using Tim's algo-1 course
"""
import sys

import pdb

class Heap:
    def __init__(self) -> None:
        self.vals = []
    
    def insert(self, elem):
        self.vals.append(elem)
        self.bubble_up()
    
    def get_min(self):
        if not self.vals:
            return None
        return self.vals[0]
    
    def delete(self, index):
        assert index < len(self.vals)
        del_val = self.vals[index]
        self.vals[index] = self.vals[-1]
        self.vals.pop()
        self.bubble_down()
        return del_val

    def extract_min(self):
        if not self.vals:
            return None
        min_val = self.vals[0]
        self.vals[0] = self.vals[-1]
        self.vals.pop()
        self.bubble_down()
        return min_val

    def heapify(self, arr):
        self.vals = arr[:]
        sz = len(self.vals)
        last_non_leaf = (sz - 1)//2
        for i in range(last_non_leaf, -1, -1):
            self.min_heapify(i)

    def bubble_up(self):
        indx = len(self.vals) - 1
        parentIdx = (indx - 1)//2
        while (indx > 0) and (self.vals[indx] < self.vals[parentIdx]):
            temp = self.vals[indx]
            self.vals[indx] = self.vals[parentIdx]
            self.vals[parentIdx] = temp
            indx = parentIdx
            parentIdx = (indx - 1)//2
    
    def bubble_down(self):
        sz = len(self.vals)
        indx = 0
        left = 2 * indx + 1
        right = 2 * indx + 2
        while left < sz:
            left_child_val = self.vals[left]
            right_child_val = sys.maxsize
            if right < sz:
                right_child_val = self.vals[right]
            parent_val = self.vals[indx]
            if (left_child_val <= right_child_val) and (left_child_val < parent_val):
                self.vals[indx] = left_child_val
                self.vals[left] = parent_val
                indx = left
            else:
                if right_child_val < parent_val:
                    self.vals[indx] = right_child_val
                    self.vals[right] = parent_val
                indx = right
                left = 2 * indx + 1
                right = 2 * indx + 2

    def min_heapify(self, index):
        if index >= len(self.vals):
            return
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if (left < len(self.vals)) and (self.vals[left] < self.vals[smallest]):
            smallest = left
        if ((right < len(self.vals)) and (self.vals[right] < self.vals[smallest])):
            smallest = right
        if smallest != index:
            self.vals[index], self.vals[smallest] = self.vals[smallest], self.vals[index]
            self.min_heapify(smallest)
