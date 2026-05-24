class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '#'.join([char for char in s])
        count = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1 if s[l] != '#' else 0
                l -= 1
                r += 1
        return count