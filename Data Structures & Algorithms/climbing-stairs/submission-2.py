class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        def rec(n, memo):
            if n <= 1:
                return 1
            if n == 2:
                return 2
            if memo[n-1]:
                return memo[n-1]
            memo[n-1] = rec(n-1, memo) + rec(n-2, memo)
            return memo[n-1]
        return rec(n, memo)