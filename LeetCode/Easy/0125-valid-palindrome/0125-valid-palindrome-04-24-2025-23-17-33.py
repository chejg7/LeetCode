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

# 아래의 방법이 더 효율적임. 
# 숫자까지 포함: str.isalnum() → 영문자·숫자 모두 인정
# O(1) 추가 공간: 새 문자열을 만들지 않고 두 포인터로 원본 문자열 직접 검사
# 효율성: lower() 변환은 비교가 필요한 글자에서만 수행 → 최소 작업
# 시간 복잡도: 여전히 O(n), 하지만 문자열 복사 비용 제거

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            # 알파벳·숫자만 비교
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
