1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        seen = set()
4        duplicates = []
5        for i in nums:
6            if i in seen:
7                duplicates.append(i)
8            else:
9                seen.add(i)
10        return duplicates