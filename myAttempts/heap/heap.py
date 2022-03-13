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
    
    def delete(self, elem):
        pass

    def extract_min(self):
        if not self.vals:
            return None
        min_val = self.vals[0]
        self.vals[0] = self.vals[-1]
        self.vals.pop()
        self.bubble_down()
        return min_val

    def heapify(self, arr):
        pass

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
        left_child_indx = 2 * indx + 1
        right_child_indx = 2 * indx + 2
        while left_child_indx < sz:
            left_child_val = self.vals[left_child_indx]
            right_child_val = sys.maxsize
            if right_child_indx < sz:
                right_child_val = self.vals[right_child_indx]
            parent_val = self.vals[indx]
            if left_child_val <= right_child_val:
                self.vals[indx] = left_child_val
                self.vals[left_child_indx] = parent_val
                indx = left_child_indx
            else:
                self.vals[indx] = right_child_val
                self.vals[right_child_indx] = parent_val
                indx = right_child_indx
            left_child_indx = 2 * indx + 1
            right_child_indx = 2 * indx + 2
        
