1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        sum_ava = sum(nums[:k])
4        max_ava = sum_ava / k 
5        for i in range(k,len(nums)):
6            sum_ava += nums[i] - nums[i-k]
7            ava = sum_ava/k
8            max_ava = max(max_ava,ava)
9            
10        return max_ava