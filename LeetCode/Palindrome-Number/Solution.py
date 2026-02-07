1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x=str(x)
4        print(x)
5        if x == x[::-1]:
6            return True
7        else:
8            return False