class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = self.to_anagrams(strs)
        hashmap = {}
        for i, ana in enumerate(anagrams):
            if ana not in hashmap:
                hashmap[ana] = [i]
            else:
                hashmap[ana].append(i)
        result = []
        for _, index_list in hashmap.items():
            sublist = [strs[i] for i in index_list]
            result.append(sublist)
        return result
    @staticmethod
    def to_anagrams(strs: List[str]) -> List[str]:
        return [''.join(sorted(str_)) for str_ in strs]
    