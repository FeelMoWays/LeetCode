class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        actual_sum = sum(nums)
        expected_sum = n * (n+1)//2
        unique_sum = sum(set(nums))
        duplicate_number = actual_sum - unique_sum
        missing_num = expected_sum - actual_sum
        return [duplicate_number,missing_num]