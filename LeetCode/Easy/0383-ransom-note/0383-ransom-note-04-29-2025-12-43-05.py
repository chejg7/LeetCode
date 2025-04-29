class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_letters = list(ransomNote)
        m_letters = list(magazine)
        for r in r_letters:
            if r not in m_letters:
                return False
            m_letters.remove(r)
        return True

# remove()와 in 연산은 리스트에서 O(n) 시간이 걸립니다.
# 전체 시간복잡도는 약 O(n²) 이 되어버려서 긴 문자열일 경우 성능이 떨어질 수 있어요.


# 아래의 코드 설명 :

# Counter는 문자열의 각 문자가 몇 번 나오는지 자동으로 세어줍니다.
# ransomNote의 각 글자에 대해 필요한 수량을 magazine이 충족하는지만 검사하면 됩니다.
# 시간복잡도는 O(n) 정도로 매우 빠릅니다.

# from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ransom_counter = Counter(ransomNote)
#         magazine_counter = Counter(magazine)
        
#         for char, count in ransom_counter.items():
#             if magazine_counter[char] < count:
#                 return False
#         return True
