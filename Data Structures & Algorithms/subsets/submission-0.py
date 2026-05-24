class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        for num in nums:
            for i in range(len(sol)):
                sol.append(sol[i] + [num])
        return sol
    