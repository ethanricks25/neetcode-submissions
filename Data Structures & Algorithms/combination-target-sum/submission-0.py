class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol = []

        def dfs(nums, i, comb, target):
            nonlocal sol
            if sum(comb) == target:
                sol.append(comb)
                return
            if sum(comb) > target or i >= len(nums):
                return
            c = comb.copy()
            c.append(nums[i])
            dfs(nums, i, c, target)
            l = c.copy()
            l.pop()
            dfs(nums, i + 1, l, target)
        dfs(nums, 0, [], target)
        return sol