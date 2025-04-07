class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        encoder = "#"
        for s in strs:
            count = 0
            for c in s:
                count += 1
            string += str(count) + "#"
            for c in s:
                string += c
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        n = len(s)

        i = 0
        while i < n:
            count_s = ""
            j = i
            while j < n and s[j] != "#":
                count_s += s[j]
                j += 1
            count = int(count_s)
            j += 1
            i = j
            string = ""
            while i < n and i < j + count:
                string += s[i]
                i += 1
            strings.append(string)
        return strings