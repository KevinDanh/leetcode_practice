class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        window = []
        for key, letter in enumerate(s):
            if letter not in window:
                window.append(letter)
            else:
                window = window[window.index(letter)+1:]
                window.append(letter)
            if len(window) > max:
                max = len(window)

        return max
        
