class Solution:
    def longestPalindrome(self, s: str) -> int:
        maxLength = 0
        addOne = False

        # Create freq map
        freqMap = {}
        for i in s:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1

        # Count highest palindrome we can make
        for i in freqMap:
            if freqMap[i] % 2 == 0:
                maxLength += freqMap[i]
            else:
                maxLength += freqMap[i] - 1
                addOne = True
    
        # Contains at least 1 odd number so we add one 
        if addOne:
            maxLength += 1 

        return maxLength
