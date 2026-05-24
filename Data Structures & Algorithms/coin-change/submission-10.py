class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount + 1)
        def dfs(a):
            if a == 0:
                return 0
            if memo[a]:
                return memo[a]
            else:
                memo[a] = float('inf')
            for coin in coins:
                if a - coin >= 0:
                    memo[a] = min(memo[a], 1 + dfs( a - coin))
            return memo[a]
        count = dfs( amount)
        return count if count < float('inf') else -1