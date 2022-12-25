import pytest

import problems.lru_cache_a1 as a1

solutions = {"attempt1": a1.LRU_Cache}

class TestLruCache:
    def test_example1(self):
        for attempt, lru_cache in solutions.items():
            print()
            cache = lru_cache(2)
            print("Empty:", cache)
            cache.put(1, 1)
            print("Only 1:", cache)
            cache.put(2, 2)
            print("1 and 2:", cache)
            assert cache.get(1) == 1, attempt
            print("1 promoted", cache)
            cache.put(3, 3)
            print("2 evicted", cache)
            # 2 should be evicted
            assert cache.get(2) == -1, attempt
            print("Same as above", cache)
            cache.put(4, 4)
            print("1 evicted", cache)
            # 1 should be evicted
            assert cache.get(1) == -1, attempt
            print("Same as above", cache)
            assert cache.get(3) == 3, attempt
            print("3 promoted", cache)
            assert cache.get(4) == 4, attempt
            print("4 promoted", cache)
    
    def test_capacity_1(self):
        for attempt, lru_cache in solutions.items():
            print()
            cache = lru_cache(1)
            print("Empty:", cache)
            assert cache.get(1) == -1, attempt
            print("Same as above:", cache)
            cache.put(1, 1)
            print("Only 1", cache)
            assert cache.get(1) == 1, attempt
            print("Same as above", cache)
            cache.put(2, 2)
            print("1 evicted", cache)
            # 1 should be evicted
            assert cache.get(1) == -1, attempt
            print("Same as above", cache)
            assert cache.get(2) == 2, attempt
            print("Same as above", cache)
            cache.put(3, 3)
            print("2 evicted", cache)
            cache.put(4, 4)
            print("3 evicted", cache)
            # Both 2 and 3 should be evicted
            assert cache.get(2) == -1, attempt
            assert cache.get(3) == -1, attempt
            assert cache.get(4) == 4, attempt
    
    def test_capacity_10(self):
        for attempt, lru_cache in solutions.items():
            print()
            cache = lru_cache(10)
            print("Empty:", cache)
            for i in range(1, 5):
                cache.put(i, i)
            print("Cache from 4 - 1:", cache)
            for i in range(5, 11):
                cache.put(i, i)
            print("Cache from 10 - 1:", cache)
            assert cache.get(5) == 5, attempt
            print("5 promoted:", cache)
            assert cache.get(9) == 9, attempt
            print("9 promoted:", cache)
            assert cache.get(11) == -1, attempt
            print("Same as above:", cache)
            cache.put(11, 11)
            print("1 evicted", cache)
            assert cache.get(1) == -1, attempt
            cache.put(12, 12)
            print("2 evicted", cache)
            cache.put(13, 13)
            print("3 evicted", cache)
            assert cache.get(4) == 4, attempt
            print("4 promoted", cache)
