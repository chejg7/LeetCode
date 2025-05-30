class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = [i for i in s.split(' ') if i != '']
        return len(str_list[-1])
