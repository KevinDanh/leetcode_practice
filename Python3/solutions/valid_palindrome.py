class Solution1:
    def isPalindrome(self, s: str) -> bool:
        lowercase_s = s.lower()
        cleaned_string="".join(character for character in lowercase_s if character.isalnum())
        left, right = 0, len(cleaned_string)-1
        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -= 1
        
        return True