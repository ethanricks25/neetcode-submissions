class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev = prev2 = 0

        for i in range(len(nums) - 1):
            tmp = prev
            prev = max(prev2 + nums[i], prev)
            prev2 = tmp
        
        res1 = prev
        prev = prev2 = 0

        for i in range(1, len(nums)):
            tmp = prev
            prev = max(prev2 + nums[i], prev)
            prev2 = tmp
        
        return res1 if res1 > prev else prev