class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = [nums[0], 1]
        while i < len(nums):
            if nums[i] == k[0]:
                k[1] += 1
                if k[1] > 2:
                    del nums[i]
                else:
                    i += 1
            else:
                k = [nums[i], 1]
                i += 1
        return i

        # 다른 풀이 : 값과 횟수를 저장하지 않고, 두 칸 앞과 다른 값이 나올 때 복사하는 방식으로 해결
        # if len(nums) <= 2:
        #     return len(nums)

        # insert_pos = 2  # 세 번째 자리부터 검사 시작

        # for i in range(2, len(nums)):
        #     # 현재 값이 두 칸 앞의 값과 같지 않다면 복사
        #     if nums[i] != nums[insert_pos - 2]:
        #         nums[insert_pos] = nums[i]
        #         insert_pos += 1

        # return insert_pos
