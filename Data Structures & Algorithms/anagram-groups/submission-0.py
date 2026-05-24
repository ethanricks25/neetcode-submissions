class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet_map = {chr(i): i - 96 for i in range(97,123)}

        d = dict()

        def create_mapping(string):
            arr = [0]*26
            for char in string:
                arr[alphabet_map[char]] += 1
            return tuple(arr)

        for string in strs:
            mapping = create_mapping(string)
            if mapping not in d:
                d[mapping] = [string]
            else:
                d[mapping].append(string)

        return list(d.values())
