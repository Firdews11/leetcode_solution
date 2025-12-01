1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        return list(set(nums1) & set(nums2))