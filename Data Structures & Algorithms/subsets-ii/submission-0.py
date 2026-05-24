class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = {()}

        for i in range(len(nums)):
            new_set = set()
            for p in sol:
                new_perm = p + tuple([nums[i]])
                new_set.add(new_perm)
            sol |= new_set

        return [list(p) for p in sol]