1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        m_p={}
4        for i ,j in enumerate(nums):
5            x = target-j
6            if x in m_p:
7                return[m_p[x],i]
8            m_p[j] = i  