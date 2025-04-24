class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ''
        for letter in s:
            if letter.isalpha():
                phrase += letter.lower()

        i, j = 0, len(phrase) - 1
        while i < j:
            if phrase[i] != phrase[j]:
                return False
            i += 1
            j -= 1
        return True
