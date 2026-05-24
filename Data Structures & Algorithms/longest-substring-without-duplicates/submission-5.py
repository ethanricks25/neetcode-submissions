class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        se = set(s[0])
        res = 0
        l = 0
        r = 1
        while r < len(s):
            if s[r] not in se:
                se.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                l += 1
                se = set(s[l:r])
        return res
    