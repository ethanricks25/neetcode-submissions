class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = prev2 = 0
        for i in range(len(nums)):
            tmp = prev
            prev = max(nums[i] + prev2, prev)
            prev2 = tmp
        return prev