# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         str_list = [i for i in s.split(' ') if i != '']
#         return len(str_list[-1])

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

# strip()으로 문자열 양쪽 공백 제거
# split()은 공백이 여러 개여도 자동으로 단어만 분리
# 마지막 단어 접근: [-1]
# 훨씬 더 간결하고 가독성이 좋음
