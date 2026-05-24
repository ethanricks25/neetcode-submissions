class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSub = nums[0]
        for i in range(1, len(nums)):
            if res < 0:
                res = 0
            res += nums[i]
            maxSub = max(res, maxSub)
        return maxSub