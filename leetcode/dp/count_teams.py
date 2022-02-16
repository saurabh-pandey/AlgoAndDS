#URL: 
#Description
"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
You have to form a team of 3 soldiers amongst them under the following rules:
Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) 
where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple 
teams).


Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 


Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.


Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
"""
def isValidTeam(i, j, k, rating):
    if (rating[i] < rating[j]) and (rating[j] < rating[k]):
        return True
    elif (rating[i] > rating[j]) and (rating[j] > rating[k]):
        return True
    return False

def numTeams_bf(rating):
    count = 0
    sz = len(rating)
    for i in range(sz):
        for j in range(i + 1, sz):
            for k in range(j + 1, sz):
                if isValidTeam(i, j, k, rating):
                    count += 1
    return count

#IDEAS
# Can we shrink the search space?
# One idea is to skip if the first pair itself doesn't meet the criterion.
# Also given first pair's ordering only check for that ordering in subsequent pairs
# Can we use a diff array or some kind of memoization?