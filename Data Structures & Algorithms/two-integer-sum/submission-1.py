class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if target / 2 == num and num in d:
                return [d[num], i]
            if d.get(target - num) != None:
                return [d.get(target - num), i]
            d[num] = i