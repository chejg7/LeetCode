class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        i = 0
        while i < len(haystack) and i + length <= len(haystack):
            if haystack[i:i + length] == needle:
                return i
            i += 1
        return -1