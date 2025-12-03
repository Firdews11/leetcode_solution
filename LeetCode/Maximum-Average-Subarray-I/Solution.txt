1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        ava = sum(nums[:k])
4        max_ava = ava / k
5        for i in range(k, len(nums)):
6            ava += nums[i]
7            ava -= nums[i-k]
8            max_ava = max(max_ava, ava / k)
9        return max_ava