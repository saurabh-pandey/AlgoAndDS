#URL: https://leetcode.com/problems/divisor-game/
#Description
"""
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move 
consisting of:
Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.


Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.


Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.


Constraints:

1 <= n <= 1000
"""
def divisorGame(n):
    AliceWinning = [False for _ in range(n)]
    # For n = 1 Alice always looses
    AliceWinning[0] = False
    # For n = 2 onwards we use past results
    for i in range(2, n + 1):
        index = i - 1
        canAliceWin = False
        for j in range(1, i):
            if i % j == 0 and not AliceWinning[i - j - 1]:
                canAliceWin = True
                break
        AliceWinning[index] = canAliceWin
    return AliceWinning[n - 1]