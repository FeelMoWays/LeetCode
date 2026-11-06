class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        sorted_nums = sorted(set(nums),reverse=True)
        if len(sorted_nums) <= 2:
            return max(sorted_nums)
        return sorted_nums[2]

#Better Time Complexity
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num in (first, second, third):
                continue

            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

        return third if third != float('-inf') else first