#URL: https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
#Description
"""
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already 
exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains 
no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for 
the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
"""
import bisect

class MyHashMap:

    def __init__(self):
        self.base_prime = 31
        self.buckets = [[]]

    def hash(self, key) -> int:
        return key % self.base_prime
    
    def put(self, key: int, value: int) -> None:
        bucket_index = self.hash(key)
        buckets_sz = len(self.buckets)
        if bucket_index >= buckets_sz:
            extended_buckets = [[] for _ in range(bucket_index - buckets_sz + 1)]
            self.buckets.extend(extended_buckets)
        bucket = self.buckets[bucket_index]
        index = bisect.bisect_left(bucket, [key, ])
        if index < len(bucket) and bucket[index][0] == key:
            bucket[index][1] = value
            return
        else:
            self.buckets[bucket_index].insert(index, [key, value])

    def get(self, key: int) -> int:
        bucket_index = self.hash(key)
        if bucket_index < len(self.buckets):
            bucket = self.buckets[bucket_index]
            index = bisect.bisect_left(bucket, [key, ])
            if index < len(bucket) and bucket[index][0] == key:
                return bucket[index][1]
        return -1

    def remove(self, key: int) -> None:
        bucket_index = self.hash(key)
        if bucket_index < len(self.buckets):
            bucket = self.buckets[bucket_index]
            index = bisect.bisect_left(bucket, [key, ])
            if index < len(bucket) and bucket[index][0] == key:
                self.buckets[bucket_index].pop(index)
