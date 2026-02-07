1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4        anagram_dic = defaultdict(list)
5        result = []
6
7        for key in strs:
8            sorted_key = tuple(sorted(key))
9            anagram_dic[sorted_key].append(key)
10        """ our dictionary {('a', 'e', 't'): ['eat', 'tea', 'ate'], ('a', 'n', 't'):   ['tan', 'nat'], ('a', 'b', 't'): ['bat']} and we used tuple b/c keys can not be lists """
11        for key in anagram_dic.values():
12            result.append(key)
13
14        return result