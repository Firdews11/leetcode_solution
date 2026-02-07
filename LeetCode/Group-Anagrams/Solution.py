1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4        anagram_dic = defaultdict(list)
5
6        for word in strs:
7            sorted_word = ''.join(sorted(word))
8            if sorted_word in anagram_dic:
9                anagram_dic[sorted_word].append(word)
10            else:
11                anagram_dic[sorted_word] = [word]
12        """ our dictionary {('a', 'e', 't'): ['eat', 'tea', 'ate'], ('a', 'n', 't'):   ['tan', 'nat'], ('a', 'b', 't'): ['bat']} and we used tuple b/c keys can not be lists """
13        
14        return list(anagram_dic.values())