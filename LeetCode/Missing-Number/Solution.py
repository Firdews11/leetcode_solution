1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        nums = sorted(nums)
4        for i in range(len(nums)):
5            if i != nums[i]:
6                return i
7        return len(nums)