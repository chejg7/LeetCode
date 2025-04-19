class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [word for word in s.split(' ') if len(word) > 0]
        return len(words[-1])
        