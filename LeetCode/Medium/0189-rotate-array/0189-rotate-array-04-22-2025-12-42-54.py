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
