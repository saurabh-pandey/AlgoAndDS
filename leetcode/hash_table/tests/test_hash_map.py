import pytest
import random

from hash_table.hash_map import MyHashMap

class TestHashMap:
    def test_example1(self):
        myHashMap = MyHashMap()
        myHashMap.put(1, 1)
        myHashMap.put(2, 2)
        assert myHashMap.get(1) == 1
        assert myHashMap.get(3) == -1
        myHashMap.put(2, 1)
        assert myHashMap.get(2) == 1
        myHashMap.remove(2)
        myHashMap.get(2) == -1
    
    def test_my1(self):
        myHashMap = MyHashMap()
        mock_map = {}
        max_key = 100000
        max_val = 10
        calls_sz = 10
        for i in range(max_key + 1):
            call_id = random.randint(0, calls_sz - 1)
            key = random.randint(0, max_key)
            if call_id < 5:
                val = random.randint(0, max_val)
                mock_map[key] = val
                myHashMap.put(key, val)
            elif call_id < 9:
                if key in mock_map:
                    assert myHashMap.get(key) == mock_map[key]
                else:
                    assert myHashMap.get(key) == -1
            else:
                mock_map.pop(key, None)
                myHashMap.remove(key)
        bucket_set = set()
        for bucket in myHashMap.buckets:
            for i in range(len(bucket)):
                num = bucket[i][0]
                if i > 0:
                    assert num >= bucket[i - 1][0], f"Inversion found at {i - 1} and {i}"
                assert num not in bucket_set, f"{num} seems to be duplicated"
                bucket_set.add(num)
        assert mock_map.keys() == bucket_set

