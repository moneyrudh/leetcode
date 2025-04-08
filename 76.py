class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        if t in s:
            return t

        n1, n2 = len(s), len(t)

        m = {}
        freq = {}

        for c in t:
            m[c] = 0
            freq[c] = freq.get(c, 0) + 1

        l, r = 0, 0
        min_count = int(1e9)
        string = []
        count = len(freq)
        string_minimum = [-1, -1]

        while r < n1:
            letter = s[r]

            if letter in m:
                m[letter] += 1
                if m[letter] == freq[letter]:
                    count -= 1

            r += 1

            while count == 0:
                if r-l+1 < min_count:
                    min_count = r-l+1
                    string_minimum = [l, r]
                if s[l] in m:
                    m[s[l]] -= 1
                    if m[s[l]] < freq[s[l]]:
                        count += 1
                l += 1

        return s[string_minimum[0]:string_minimum[1]]