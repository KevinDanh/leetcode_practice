from typing import List
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapAnagrams = {}

        for i in strs:
            word = ''.join(sorted(i))
            if word not in mapAnagrams:
                mapAnagrams[word] = [i]
            else:
                mapAnagrams[word].append(i)

        return list(mapAnagrams.values())