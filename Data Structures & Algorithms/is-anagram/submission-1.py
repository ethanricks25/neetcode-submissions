class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0] * len(s)
        ds = dict(zip(s,arr) )
        dr = dict(zip(t,arr))

        for char in s:
            ds[char] += 1

        for char in t:
            dr[char] += 1

        return ds == dr


