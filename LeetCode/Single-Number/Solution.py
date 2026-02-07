1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        n = 0 
4        for i in nums:
5            n^=i 
6        return n
7        # the sign ^ is bitt=wise XOR perform bits of 2 integer
8