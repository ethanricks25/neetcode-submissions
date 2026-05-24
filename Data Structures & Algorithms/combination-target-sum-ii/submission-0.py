class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()
        def dfs(i, comb, total):
            nonlocal sol
            if total == target:
                sol.append(comb.copy())
                return

            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                comb.append(candidates[j])
                dfs(j + 1, comb, total + candidates[j])
                comb.pop()
            return
        dfs(0, [], 0)
        return sol
        