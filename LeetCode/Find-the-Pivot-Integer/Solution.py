1class Solution:
2    def pivotInteger(self, n: int) -> int:
3        for i in range(n,-1,-1):
4            a=((n*(n+1)/2)-(i*(i-1)/2))
5            b=((i*(i+1)/2))
6            if a==b:
7                return i
8        return -1