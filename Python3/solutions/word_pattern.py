class Solution1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        split_string = s.split(' ') # split up each word in s
        used_values = []
        if len(pattern) != len(split_string):
            return False
        for k,v in enumerate(pattern):
            if pattern[k] not in map and split_string[k] not in used_values:
                map[pattern[k]] = split_string[k]
                used_values.append(split_string[k])
            elif pattern[k] not in map and split_string[k] in used_values:
                return False
            elif pattern[k] in map and split_string[k] != map[pattern[k]]:
                return False
        return True