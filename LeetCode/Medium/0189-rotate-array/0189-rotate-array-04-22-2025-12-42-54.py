class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums2 = []
        # for i in range(len(nums)):
        #     nums2.append(nums[i - k])
        # nums[:] = nums2[:]
        # in-place 조건 위반, k가 리스트 길이를 초과할 때에 대한 처리가 없음

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        # 공간복잡도 O(1)으로 풀 수 있는 방법(리스트를 세 번 뒤집음)
        # def reverse(start, end):
        #     while start < end:
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1

        # n = len(nums)
        # k %= n

        # reverse(0, n - 1)
        # reverse(0, k - 1)
        # reverse(k, n - 1)
