1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        k = len(p)
4        ans =[]
5        target = Counter(p)
6        window = Counter(s[:k])
7        if window == target:
8            ans.append(0)
9        for i in range(k, len(s)):
10            window[s[i - k]] -= 1
11            window[s[i]] += 1
12            if window == target:
13                ans.append(i - k + 1)
14        return ans 
15