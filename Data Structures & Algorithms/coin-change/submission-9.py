class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount + 1)
        def dfs(a):
            if a == 0:
                return 0
            if memo[a]:
                return memo[a]
            best = float('inf')
            for coin in coins:
                if a - coin >= 0:
                    best = min(best, 1 + dfs( a - coin))
            memo[a] = best
            return best
        count = dfs( amount)
        return count if count < float('inf') else -1