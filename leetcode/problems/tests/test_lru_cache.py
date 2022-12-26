import pytest

from typing import Dict

import problems.lru_cache_a1 as a1

solutions = {"attempt1": a1.LRU_Cache}

class TestLruCache:
    def _compare_dict(self, actual: Dict, expected: Dict):
        for (k1, v1), (k2, v2) in zip(actual.items(), expected.items()):
            if k1 != k2:
                return False
            elif v1 != v2:
                return False
        return True
    
    def _compare_cache_order(self, actual: Dict, expected: Dict):
        if not self._compare_dict(actual["forward"], expected["forward"]):
            return False
        if not self._compare_dict(actual["reverse"], expected["reverse"]):
            return False
        return True
    
    def _make_two_way_cache_order(self, expected_forward_order: Dict[int,int]):
        two_way_order = {}
        two_way_order["forward"] = expected_forward_order
        two_way_order["reverse"] = {
            k: v for (k, v) in reversed(expected_forward_order.items())
        }
        return two_way_order
    
    def _check_cache(
            self,
            cache: a1.LRU_Cache,
            expected_key_val: Dict,
            expected_cache_order: Dict,
            attempt: str):
        assert self._compare_dict(cache.lookup_dict(),expected_key_val), attempt
        assert self._compare_cache_order(
            cache.cache_order(),
            self._make_two_way_cache_order(expected_cache_order)), attempt


    def test_example1(self):
        for attempt, lru_cache in solutions.items():
            cache = lru_cache(2)
            self._check_cache(cache, {}, {}, attempt)
            cache.put(1, 1)
            self._check_cache(cache, {1:1}, {1:1}, attempt)
            cache.put(2, 2)
            self._check_cache(cache, {1:1, 2:2}, {2:2, 1:1}, attempt)
            assert cache.get(1) == 1, attempt
            self._check_cache(cache, {1:1, 2:2}, {1:1, 2:2}, attempt)
            cache.put(3, 3)
            self._check_cache(cache, {1:1, 3:3}, {3:3, 1:1}, attempt)
            assert cache.get(2) == -1, attempt
            self._check_cache(cache, {1:1, 3:3}, {3:3, 1:1}, attempt)
            cache.put(4, 4)
            self._check_cache(cache, {3:3, 4:4}, {4:4, 3:3}, attempt)
            assert cache.get(1) == -1, attempt
            self._check_cache(cache, {3:3, 4:4}, {4:4, 3:3}, attempt)
            assert cache.get(3) == 3, attempt
            self._check_cache(cache, {3:3, 4:4}, {3:3, 4:4}, attempt)
            assert cache.get(4) == 4, attempt
            self._check_cache(cache, {3:3, 4:4}, {4:4, 3:3}, attempt)
    
    def test_capacity_1(self):
        for attempt, lru_cache in solutions.items():
            cache = lru_cache(1)
            self._check_cache(cache, {}, {}, attempt)
            assert cache.get(1) == -1, attempt
            self._check_cache(cache, {}, {}, attempt)
            cache.put(1, 1)
            self._check_cache(cache, {1:1}, {1:1}, attempt)
            assert cache.get(1) == 1, attempt
            self._check_cache(cache, {1:1}, {1:1}, attempt)
            cache.put(2, 2)
            self._check_cache(cache, {2:2}, {2:2}, attempt)
            assert cache.get(1) == -1, attempt
            self._check_cache(cache, {2:2}, {2:2}, attempt)
            assert cache.get(2) == 2, attempt
            self._check_cache(cache, {2:2}, {2:2}, attempt)
            cache.put(3, 3)
            self._check_cache(cache, {3:3}, {3:3}, attempt)
            cache.put(4, 4)
            self._check_cache(cache, {4:4}, {4:4}, attempt)
            assert cache.get(2) == -1, attempt
            self._check_cache(cache, {4:4}, {4:4}, attempt)
            assert cache.get(3) == -1, attempt
            self._check_cache(cache, {4:4}, {4:4}, attempt)
            assert cache.get(4) == 4, attempt
            self._check_cache(cache, {4:4}, {4:4}, attempt)
    
    def test_capacity_10(self):
        for attempt, lru_cache in solutions.items():
            cache = lru_cache(10)
            self._check_cache(cache, {}, {}, attempt)
            for i in range(1, 5):
                cache.put(i, i)
            self._check_cache(cache,
                              {1:1, 2:2, 3:3, 4:4},
                              {4:4, 3:3, 2:2, 1:1},
                              attempt)
            for i in range(5, 11):
                cache.put(i, i)
            self._check_cache(
                cache,
                {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10},
                {10:10, 9:9, 8:8, 7:7, 6:6, 5:5, 4:4, 3:3, 2:2, 1:1},
                attempt)
            assert cache.get(5) == 5, attempt
            self._check_cache(
                cache,
                {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10},
                {5:5, 10:10, 9:9, 8:8, 7:7, 6:6, 4:4, 3:3, 2:2, 1:1},
                attempt)
            assert cache.get(9) == 9, attempt
            self._check_cache(
                cache,
                {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10},
                {9:9, 5:5, 10:10, 8:8, 7:7, 6:6, 4:4, 3:3, 2:2, 1:1},
                attempt)
            assert cache.get(11) == -1, attempt
            self._check_cache(
                cache,
                {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10},
                {9:9, 5:5, 10:10, 8:8, 7:7, 6:6, 4:4, 3:3, 2:2, 1:1},
                attempt)
            cache.put(11, 11)
            self._check_cache(
                cache,
                {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11},
                {11:11, 9:9, 5:5, 10:10, 8:8, 7:7, 6:6, 4:4, 3:3, 2:2},
                attempt)
            assert cache.get(1) == -1, attempt
            self._check_cache(
                cache,
                {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11},
                {11:11, 9:9, 5:5, 10:10, 8:8, 7:7, 6:6, 4:4, 3:3, 2:2},
                attempt)
            cache.put(12, 12)
            self._check_cache(
                cache,
                {3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12},
                {12:12, 11:11, 9:9, 5:5, 10:10, 8:8, 7:7, 6:6, 4:4, 3:3},
                attempt)
            cache.put(13, 13)
            self._check_cache(
                cache,
                {4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13},
                {13:13, 12:12, 11:11, 9:9, 5:5, 10:10, 8:8, 7:7, 6:6, 4:4},
                attempt)
            assert cache.get(4) == 4, attempt
            self._check_cache(
                cache,
                {4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13},
                {4:4, 13:13, 12:12, 11:11, 9:9, 5:5, 10:10, 8:8, 7:7, 6:6},
                attempt)
            assert cache.get(12) == 12, attempt
            self._check_cache(
                cache,
                {4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13},
                {12:12, 4:4, 13:13, 11:11, 9:9, 5:5, 10:10, 8:8, 7:7, 6:6},
                attempt)
