#URL: https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
#Description
"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of 
favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a 
choice tie between answers, output all of them with no order requirement. You could assume there 
always exists an answer.


Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at 
Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".


Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger 
King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 
1 (0+1).


Constraints:

1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the stings of list1 are unique.
All the stings of list2 are unique.
"""
def findRestaurant(list1, list2):
    sz1 = len(list1)
    sz2 = len(list2)
    restaurant_map = {}
    for i in range(sz1):
        restaurant = list1[i]
        restaurant_map[restaurant] = i
    filtered_restaurant = []
    min_index = sz1 + sz2
    for i in range(sz2):
        restaurant = list2[i]
        if restaurant in restaurant_map:
            index = i + restaurant_map[restaurant]
            if index < min_index:
                filtered_restaurant.clear()
                min_index = index
                filtered_restaurant.append(restaurant)
            elif index == min_index:
                filtered_restaurant.append(restaurant)
    return filtered_restaurant
    

