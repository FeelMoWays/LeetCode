class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums = sorted(nums)
        median = nums[len(nums) >> 1]
        total_moves = sum(abs(num - median) for num in nums)
        return total_moves