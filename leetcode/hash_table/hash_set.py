#URL: https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
#Description
"""
Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do 
nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""

from pdb import set_trace
import bisect


class MyHashSet:
    def __init__(self) -> None:
        self.base_prime = 99877
        self.buckets = [[]]
    
    def hash(self, key) -> int:
        return key % self.base_prime

    def add(self, key) -> None:
        bucket_index = self.hash(key)
        sz = len(self.buckets)
        if bucket_index >= sz:
            extended_buckets = [[] for _ in range(bucket_index - sz + 1)]
            self.buckets.extend(extended_buckets)
        bucket = self.buckets[bucket_index]
        index = bisect.bisect_left(bucket, key)
        if index != len(bucket) and bucket[index] == key:
            return
        else:
            self.buckets[bucket_index].insert(index, key)

    def remove(self, key) -> None:
        bucket_index = self.hash(key)
        sz = len(self.buckets)
        if bucket_index < sz:
            bucket = self.buckets[bucket_index]
            index = bisect.bisect_left(bucket, key)
            if index != len(bucket) and bucket[index] == key:
                self.buckets[bucket_index].pop(index)

    def contains(self, key) -> bool:
        bucket_index = self.hash(key)
        sz = len(self.buckets)
        if bucket_index < sz:
            bucket = self.buckets[bucket_index]
            index = bisect.bisect_left(bucket, key)
            if index != len(bucket) and bucket[index] == key:
                return True
        return False
