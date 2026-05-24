class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        suff, pre = 0, 0

        for i in range(len(nums)):
            pre = nums[i] * (pre or 1)
            suff = nums[len(nums) - 1 - i] * (suff or 1)
            res = max(res, pre, suff)
        return res
