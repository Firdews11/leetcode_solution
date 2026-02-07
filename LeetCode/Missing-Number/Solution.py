1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4        return n*(n+1)//2 - sum(nums)