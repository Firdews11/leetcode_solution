1class Solution:
2    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
3        arr.sort()
4        differ = arr[1] - arr[0]
5        for i in range(1,len(arr)-1):
6            diff = arr[i+1] - arr[i] 
7            if differ != diff:
8                return False
9        return True
10