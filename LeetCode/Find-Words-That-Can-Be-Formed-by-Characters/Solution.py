1class Solution:
2    def countCharacters(self, words: List[str], chars: str) -> int:
3        length = 0
4        chars_count = Counter(chars)
5
6        for word in words:
7            word_count = Counter(word)  
8            x = True
9            for letter, count in word_count.items():
10                if count > chars_count.get(letter, 0):
11                    x = False
12                    break
13            if x:
14                length += len(word)
15
16        return length
17