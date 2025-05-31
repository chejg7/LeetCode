# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         num = int(''.join([str(i) for i in digits])) + 1
#         return [int(s) for s in list(str(num))]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# 뒤에서부터 숫자를 올림 처리
# 9일 경우 0으로 바꾸고 자리 올림
# 전부 9일 경우 [1, 0, 0, ..., 0] 반환
# ⏱ 시간 복잡도는 O(n) 이고, 문자열 변환 없이 처리 가능하므로 더 최적화된 방법입니다.
