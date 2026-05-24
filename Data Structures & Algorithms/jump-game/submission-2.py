class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        lastIndex = len(nums) - 1
        dp[lastIndex] = True

        for i in range(lastIndex - 1, -1, -1):
            if nums[i] >= lastIndex - i:
                dp[i] = True
                lastIndex = i
        return dp[0]