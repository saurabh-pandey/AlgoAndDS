#URL: https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1058/
#Description
"""
Design a map that allows you to do the following:
Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:
MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, 
the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.


Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
 

Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""

class MapSum:

    def __init__(self):
        self.children = {}
        self.val = 0

    
    def insert(self, key: str, val: int) -> None:
        currNode = self
        for k in key:
            if k in self.children:
                currNode = currNode.children[k]
            else:
                new_node = MapSum()
                currNode.children[k] = new_node
                currNode = new_node
        currNode.val = val

    
    def sum(self, prefix: str) -> int:
        curr_node = self
        for p in prefix:
            if p not in curr_node.children:
                return 0
            else:
                curr_node = curr_node.children[p]
        calc_sum = 0
        nodes = [curr_node]
        while not nodes:
            node = nodes.pop(0)
            calc_sum += node.val
            nodes.extend(node.children)
        return calc_sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)