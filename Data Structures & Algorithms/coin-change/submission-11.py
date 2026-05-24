class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount+1)
        memo[0] = 0
        for a in range(1, amount +1):
            for coin in coins:
                if a - coin >= 0:
                    memo[a] = min(memo[a], memo[a-coin] + 1)
        return memo[amount] if memo[amount] < float('inf') else -1