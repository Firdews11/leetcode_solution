1class Solution:
2    def pivotInteger(self, n: int) -> int:
3        total = (n*(n +1)) //2
4        for i in range(n+1):
5            center = i * (i+1) //2
6            if center == (total - center +i):
7                return i
8
9        return -1
10