#URL: https://leetcode.com/problems/lru-cache/
"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.


Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""
from typing import List, Union

class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    

class DoublyLinkedList:
    def __init__(self) -> None:
        self._begin = None
        self._end = None

    def add(self, key: int, val: int) -> Node:
        n = Node(key, val)
        if self._begin is not None:
            self._begin.prev = n
        n.next = self._begin
        self._begin = n
        if self._end is None:
            self._end = n
        return n
    
    def promote(self, n: Node) -> None:
        if n.prev is None:
            return
        else:
            n.prev.next = n.next
            if n.next is not None:
                n.next.prev = n.prev
            else:
                assert n == self._end, "Last node is not the end pointer"
                self._end = n.prev
            self._begin.prev = n
            n.next = self._begin
            n.prev = None
            self._begin = n
    
    def evict(self) -> Union[Node, None]:
        assert self._end is not None, "Can't evict empty list"
        n = self._end
        if n == self._begin:
            self._begin = None
            self._end = None
        else:
            self._end = n.prev
            self._end.next = None
        return n
    
    def __str__(self) -> str:
        list_str = "\nForward: "
        curr = self._begin
        while curr is not None:
            list_str += f"{{{curr.key}:{curr.val}}}"
            curr = curr.next
        list_str += "\nBackward: "
        curr = self._end
        while curr is not None:
            list_str += f"{{{curr.key}:{curr.val}}}"
            curr = curr.prev
        return list_str
    
    def node_order(self):
        node_dict = {"forward": {}, "reverse": {}}
        curr_node = self._begin
        while curr_node is not None:
            node_dict["forward"][curr_node.key] = curr_node.val
            curr_node = curr_node.next
        curr_node = self._end
        while curr_node is not None:
            node_dict["reverse"][curr_node.key] = curr_node.val
            curr_node = curr_node.prev
        return node_dict


class LRU_Cache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._list = DoublyLinkedList()
        self._key_val = {}

    def get(self, key: int) -> int:
        if key in self._key_val:
            n = self._key_val[key]
            self._list.promote(n)
            return n.val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key in self._key_val:
            n = self._key_val[key]
            n.val = val
            self._list.promote(n)
        else:
            if len(self._key_val) == self._capacity:
                n = self._list.evict()
                del self._key_val[n.key]
            n = self._list.add(key, val)
            self._key_val[key] = n
    
    def __str__(self) -> str:
        key_val_dict = {}
        for key, node in self._key_val.items():
            key_val_dict[key] = node.val
        cache_state = ""
        cache_state += "\nDict = " + str(key_val_dict)
        cache_state += "\nList:" + str(self._list)
        cache_state += "\n"
        return cache_state
    
    def lookup_dict(self):
        key_val_dict = {}
        for key, n in self._key_val.items():
            key_val_dict[key] = n.val
        return key_val_dict
    
    def cache_order(self):
        return self._list.node_order()
    
