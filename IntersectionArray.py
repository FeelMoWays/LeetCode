class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        return list(set_1 & set_2)