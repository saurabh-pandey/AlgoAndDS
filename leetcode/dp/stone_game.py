#URL: https://leetcode.com/problems/stone-game/
#Description
"""
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a 
row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones. The total number of stones across all the 
piles is odd, so there are no ties.
Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of 
stones either from the beginning or from the end of the row. This continues until there are no more 
piles left, at which point the person with the most stones wins.
Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.


Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.


Example 2:

Input: piles = [3,7,2,3]
Output: true


Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.
"""
def stoneGameRecursive(piles, s, e, alice_count, bob_count):
    if s > e:
        return (alice_count, bob_count)
    results = []
    for i in [0, 1]:
        for j in [0, 1]:
            if i == 0 and j == 0:
                alice_count += piles[s]
                s += 1
                bob_count += piles[s]
                s += 1
                alice_res, bob_res = stoneGameRecursive(piles, s, e, alice_count, bob_count)
                results.append[(alice_res, bob_res)]
            if i == 0 and j == 1:
                alice_count += piles[s]
                s += 1
                bob_count += piles[e]
                e -= 1
                alice_res, bob_res = stoneGameRecursive(piles, s, e, alice_count, bob_count)
                results.append[(alice_res, bob_res)]
            if i == 1 and j == 0:
                alice_count += piles[e]
                e -= 1
                bob_count += piles[s]
                s += 1
                alice_res, bob_res = stoneGameRecursive(piles, s, e, alice_count, bob_count)
                results.append[(alice_res, bob_res)]
            if i == 1 and j == 1:
                alice_count += piles[e]
                e -= 1
                bob_count += piles[e]
                e -= 1
                alice_res, bob_res = stoneGameRecursive(piles, s, e, alice_count, bob_count)
                results.append[(alice_res, bob_res)]
    for alice_res, bob_res in results:
        if alice_res > bob_res:
            return True
    return False



def stoneGame(piles):
    print("\nPiles = ", piles)
    sz = len(piles)
    coll_sz = (sz//2) + 1
    alice_collection = [0 for _ in range(coll_sz)]
    bob_collection = [0 for _ in range(coll_sz)]
    s = 0
    e = sz - 1
    alice_count = 1
    alice_chance = True
    bob_count = 1
    while s <= e:
        if alice_chance:
            sum1 = piles[s] + alice_collection[alice_count - 1]
            sum2 = piles[e] + alice_collection[alice_count - 1]
            if sum1 < sum2:
                alice_collection[alice_count] = sum2
                e -= 1
            else:
                alice_collection[alice_count] = sum1
                s += 1
            alice_count += 1
            alice_chance = False
        else:
            sum1 = piles[s] + bob_collection[bob_count - 1]
            sum2 = piles[e] + bob_collection[bob_count - 1]
            if sum1 < sum2:
                bob_collection[bob_count] = sum2
                e -= 1
            else:
                bob_collection[bob_count] = sum1
                s += 1
            bob_count += 1
            alice_chance = True
    print("Alice = ", alice_collection)
    print("Bob   = ", bob_collection)
    return alice_collection[-1] > bob_collection[-1]
