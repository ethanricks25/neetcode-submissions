class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) == 1:
            return s if t in s else ""

        t_map = dict()

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        d = dict()
        l = 0
        st = set()

        for r in range(len(s)):
            if s[r] in t:
                d[s[r]] = d.get(s[r], 0) + 1
            while all([d.get(char) != None and d.get(char) >= t_map[char] for char in t]):
                st.add(s[l:r+1])
                if s[l] in t:
                    d[s[l]] -= 1
                l += 1
        return min(st, key=len) if not len(st) == 0 else ""
