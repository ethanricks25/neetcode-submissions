class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = [0] * len(nums)
        count = 0

        for num in nums:
            if num != 0:
                product *= num
            elif num == 0:
                count += 1

        if count > 1:
            return [0] * len(nums)
        
        for i, num in enumerate(nums):
            if 0 in nums and not nums[i] == 0:
                output[i] = 0
            if nums[i] == 0:
                output[i] = int(product)
            if 0 not in nums:
                output[i] = int(product * (num ** -1))
        
        return output
            