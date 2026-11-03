class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_value = max(nums)
        return sum((i - max_value )for i in nums)

#Maybe a better time complexity
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums)