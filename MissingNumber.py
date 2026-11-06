class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) + 1
        actual_sum = sum(nums)
        expected_sum = (n*(n+1))//2
        return expected_sum - actual_sum