1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x=str(x)
4        return x == x[::-1]
5