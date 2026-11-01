class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = -1
        votes = 0
        n = len(nums)
        for i in range(n):
            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                if nums[i] == candidate:
                    votes += 1
                else:
                    votes -= 1
        count = 0

        for i in range(n):
            if (nums[i] == candidate):
                count += 1
        if count > n//2:
            return candidate
        else:
            return -1