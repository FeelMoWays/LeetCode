class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_value = min(nums)
        sum_values = sum(nums)
        return sum_values - (min_value * len(nums))