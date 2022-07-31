# Time Complexity O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        open_brace = ['(', '[', '{']
        close_brace = [')', ']', '}']
        stack = []
        for i in range(len(s)):
            if s[i] in open_brace:
                stack.append(open_brace.index(s[i]))
                continue
            if stack and close_brace.index(s[i]) == stack.pop():
                pass
            else:
                return False
        if (len(stack) > 0):
            return False
        else:
            return True
        