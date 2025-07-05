class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(32):  # 32비트 정수의 각 비트 위치
            bit_sum = 0
            for num in nums:
                # 해당 비트가 켜져 있으면 1 더하기
                bit_sum += (num >> i) & 1

            # 3으로 나눈 나머지가 1이라면, 해당 비트가 정답 숫자에 있음
            if bit_sum % 3 != 0:
                result |= (1 << i)

        # 음수 처리 (파이썬은 음수를 2의 보수로 표현하지 않으므로 보정 필요)
        if result >= 2**31:
            result -= 2**32

        return result


# | 아이디어                | 설명            |
# | ------------------- | ------------- |
# | 각 비트 위치마다 합산        | 1이 등장한 횟수를 센다 |
# | % 3 후 1이면 정답의 해당 비트 | 사라지지 않고 남는 비트 |
# | 최종 숫자 조립            | 비트를 모아 숫자 완성  |
