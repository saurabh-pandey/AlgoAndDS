import pytest

import hash_table.min_list_index_sum as prob


class TestMinListIndexSum:
    def test_example1(self):
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        res = ["Shogun"]
        assert prob.findRestaurant(list1, list2) == res
    
    def test_example2(self):
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["KFC","Shogun","Burger King"]
        res = ["Shogun"]
        assert prob.findRestaurant(list1, list2) == res
    
    def test_my1(self):
        list1 = ["Tapioca Express","Burger King","Shogun","KFC"]
        list2 = ["KFC","Shogun","Burger King"]
        res = ["KFC","Shogun","Burger King"]
        assert set(prob.findRestaurant(list1, list2)) == set(res)