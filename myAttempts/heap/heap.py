#Description
"""
A heap data structure. It supports the follwoing operations:
insert(elem) => O(log N)
extract_min() => O(log N)
delete(N) => O(log N)
heapify(arr) => O(N)

NOTE: This is using Tim's algo-1 course
"""

class Heap:
    def __init__(self) -> None:
        self.vals = []
    
    def insert(self, elem):
        self.vals.append(elem)
        self.bubble_up()
        print(self.vals)
    
    def get_min(self):
        # self.vals.append(elem)
        # self.bubble_up()
        pass
    
    def delete(self, elem):
        pass

    def extract_min(self):
        if not self.vals:
            return None
        return self.vals[0]

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

