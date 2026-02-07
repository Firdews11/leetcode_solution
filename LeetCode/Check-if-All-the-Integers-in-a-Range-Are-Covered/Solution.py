1class Solution:
2    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
3        for x in range(left, right + 1):
4            if not any(start <= x <= end for start, end in ranges):
5                return False
6        return True