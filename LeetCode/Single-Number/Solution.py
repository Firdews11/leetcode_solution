1class Solution(object):
2    def singleNumber(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        # n=0
8        # for i in nums:
9        #     n= n^i
10        # return n
11        for i in nums:
12            if nums.count(i)==1:
13                return i
14        