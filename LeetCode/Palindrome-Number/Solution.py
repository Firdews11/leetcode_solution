1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x = str(x)
4        if x == x[::-1]:
5            return True
6        return False 