class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if r - l == 1:
                return nums[l] if nums[l] < nums[r] else nums[r]
            elif nums[m] > nums[r]:
                l = m
            elif nums[m] <= nums[l]:
                r = m
        return nums[l]