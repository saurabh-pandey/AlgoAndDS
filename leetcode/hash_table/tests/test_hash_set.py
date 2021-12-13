import pytest
import random

from hash_table.hash_set import MyHashSet


class TestHashSet:
    def test_example1(self):
        myHashSet = MyHashSet()
        myHashSet.add(1)
        myHashSet.add(2)
        assert myHashSet.contains(1) == True
        assert myHashSet.contains(3) == False
        myHashSet.add(2)
        assert myHashSet.contains(2) == True
        myHashSet.remove(2)
        assert myHashSet.contains(2) == False
    
    def test_my1(self):
        myHashSet = MyHashSet()
        mock_set = set()
        max_num = 100
        calls_sz = 10
        for i in range(max_num + 1):
            call_id = random.randint(0, calls_sz - 1)
            num = random.randint(0, max_num)
            if call_id < 5:
                mock_set.add(num)
                myHashSet.add(num)
            elif call_id < 9:
                if num in mock_set:
                    assert myHashSet.contains(num) == True
                else:
                    assert myHashSet.contains(num) == False
            else:
                mock_set.discard(num)
                myHashSet.remove(num)
        bucket_set = set()
        for bucket in myHashSet.buckets:
            for num in bucket:
                if num in bucket_set:
                    print("WARNING: {num} seems to be duplicated")
                bucket_set.add(num)
        
        print()
        print(mock_set)
        print(myHashSet.buckets)
        print(bucket_set)
